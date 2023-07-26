from django import forms
from django.conf import settings


class ConvenientFormsetsBase():
    deletion_widget = forms.HiddenInput
    ordering_widget = forms.HiddenInput

    @property
    def media(self):
        """
        Returns a `Media` object that includes the form's media together with
        the JavaScript required for in-browser interaction.
        """
        js_extension = "js"
        convenient_formsets_media = forms.Media(
            js=(f"convenient_formsets/convenient_formsets.{js_extension}",)
        )
        forms_media = super().media
        return convenient_formsets_media + forms_media


class ConvenientBaseFormSet(ConvenientFormsetsBase, forms.BaseFormSet):
    pass


class ConvenientBaseModelFormSet(ConvenientFormsetsBase, forms.BaseModelFormSet):
    pass


class ConvenientBaseInlineFormSet(ConvenientFormsetsBase, forms.BaseInlineFormSet):
    pass
