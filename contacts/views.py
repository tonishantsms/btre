from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        
        listings = request.POST("listings")
        listing_id = request.POST("listing_id")
        name = request.POST("name")
        email = request.POST("email")
        phone = request.POST("phone")
        message = request.POST("messsage")
        user_id = request.POST("user_id")
        relator_email = request.POST("relator_email")

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email= email, message= message, user_id = user_id)

        contact.save()

        message.success(request, "Your request has been submitted   ")

        return redirect('/listings/'+listing_id)