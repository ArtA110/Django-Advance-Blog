{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
<h1>Welcome to my blog mailing system!</h1>
<hr>
<img src="https://avatars.githubusercontent.com/u/65806485?s=400&u=149480b3e9c3b1e5cf193fe7e6da63fd86b1adbc&v=4" />
{% endblock %}