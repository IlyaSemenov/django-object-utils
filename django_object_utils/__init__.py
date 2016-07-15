def reload_object(obj):
	"""
	Reload object in-place with the latest version from the database.
	"""
	obj.__dict__ = obj.__class__.objects.get(pk=obj.pk).__dict__


def lock_object(obj):
	"""
	Enter a critical section and ensure that the object is the latest version.
	Use the corresponding database row as the synchronization monitor.
	"""
	if not hasattr(obj, '_locked'):
		obj.__dict__ = obj.__class__.objects.select_for_update().get(pk=obj.pk).__dict__
		obj._locked = True
	return obj


def update_object(obj, **kwargs):
	"""
	update_object(user, email='john@gmail.com')  # Run SQL UPDATE for certain fields only and update the Python object
	update_object(user, balance=F('balance')+payment, reload=True)  # Run SQL UPDATE and then reload the object from the database
	"""
	do_reload = kwargs.pop('reload', False)
	# TODO: support reload__exact for fields named Model.reload
	updated = obj.__class__.objects.filter(pk=obj.pk).update(**kwargs) > 0
	if updated:
		if do_reload:
			reload_object(obj)
		else:
			for k, v in kwargs.items():
				setattr(obj, k, v)
	return updated
