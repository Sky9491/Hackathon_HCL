from django.contrib import admin
from .models import UserProfile

# Custom admin for UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user', 'phone_number', 'kyc_file_link', 'created_at', 'kyc_verified_status')
    
    # Fields you can search by
    search_fields = ('user__username', 'user__email', 'phone_number')
    
    # Filters on the right sidebar
    list_filter = ('created_at', )
    
    # Make some fields read-only
    readonly_fields = ('created_at',)
    
    # Custom method to display KYC document as a link
    def kyc_file_link(self, obj):
        if obj.kyc_document:
            return f'<a href="{obj.kyc_document.url}" target="_blank">View KYC</a>'
        return 'No Document'
    kyc_file_link.allow_tags = True
    kyc_file_link.short_description = 'KYC Document'

    # Custom method for KYC verification status (simulated here)
    def kyc_verified_status(self, obj):
        # If you don't have a boolean field yet, let's simulate
        return 'Verified ✅' if hasattr(obj, 'kyc_verified') and obj.kyc_verified else 'Pending ⏳'
    kyc_verified_status.short_description = 'KYC Status'

    # Optional: add ordering
    ordering = ('-created_at',)
