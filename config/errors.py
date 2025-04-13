from django.shortcuts import render

from django.views import View


class PageNotFoundView(View):
    """
    View for handling 404 errors.
    """

    template_name = '404.html'
    status_code = 404

    def get(self, request, exception=None, *args, **kwargs):
        """
        Render the 404 template.
        """
        return render(request, self.template_name, status=self.status_code)


page_not_found_as_view = PageNotFoundView.as_view()
