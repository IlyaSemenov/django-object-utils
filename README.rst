django-object-utils
===================

This small library provides helpers for updating Django model objects without race conditions.


Installation
============

::

        pip install django-object-utils


Usage
=====

.. code:: python

	from django_object_utils import reload_object, update_object, lock_object

	user = User.objects.get(pk=1)

	# Reload object in-place with the latest version from the database
	reload_object(user)

	# Run SQL UPDATE for certain fields only and update the Python object
	update_object(user, username='john', email='john@gmail.com')
	
	# Run SQL UPDATE and then reload the object from the database
	update_object(user, balance=F('balance')+payment, reload=True)

	if request.method == 'POST':
		with transaction.atomic():
			# Enter a critical section and ensure that the object is the latest version.
			# Use the corresponding database row as the synchronization monitor.
			lock_object(user)
			form = UserForm(data=request.METHOD)
			form.save()
