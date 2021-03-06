from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        try:
            return self.request.user.login_method == "email"
        except AttributeError:
            pass

    def handle_no_permission(self):
        messages.error(self.request, "사이트전용 회원만 가능합니다.")
        return redirect("core:home")


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "이미 로그인되어 있습니다.")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    # login_url = reverse_lazy("users:login")
    def handle_no_permission(self):
        messages.error(self.request, "로그인이 필요합니다.")
        return redirect("users:login")