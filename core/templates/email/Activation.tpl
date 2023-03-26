{% extends "mail_templated/base.tpl" %}

{% block subject %}
Please Activate your account
{% endblock %}

{% block html %}
<h1>Please Verify</h1>
<hr>
<p>Click on <a href="http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{ token }}">This Link</a> to Verify your account</p>
{% endblock %}