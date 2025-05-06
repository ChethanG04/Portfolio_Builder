from django.shortcuts import render, redirect
from .models import PortfolioEntry

# View to render the portfolio form
def show_portfolio_form(request):
    return render(request, 'portfolio/portfolio_form.html')

# View to handle form submission
def save_portfolio(request):
    if request.method == 'POST':
        # Get data from HTML form
        full_name = request.POST.get('full_name')
        job_title = request.POST.get('job_title')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        website = request.POST.get('website')
        summary = request.POST.get('summary')

        # Save into database
        PortfolioEntry.objects.create(
            full_name=full_name,
            job_title=job_title,
            email=email,
            phone=phone,
            location=location,
            website=website,
            summary=summary
        )

        # Redirect to success page after form submission
        return redirect('success')  # Redirect to the success page

    return render(request, 'portfolio/portfolio_form.html')  # Render the form page for GET requests

# View for success page after form submission
def success(request):
    return render(request, 'portfolio/success.html')  # Show the success page after submission
