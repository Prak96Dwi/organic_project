""" apps/shipping/views.py """
from django.shortcuts import render
from apps.shipping.forms import ShippingForm


def shipping_form_page(request):
	"""
	This function is used to shipping form
	to the admin
	"""
	if request.method == 'POST':
		shipping_form = ShippingForm(request.POST)
		if shipping_form.is_valid():
			shipping_form.save()
			return redirect('admin_dashboard_page')
	else:
		shipping_form = ShippingForm()

	return render(request, 'admin/shipping_form.html', {'form': shipping_form})
