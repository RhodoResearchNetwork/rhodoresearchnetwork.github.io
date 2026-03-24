---
layout: debug
title: "Debug"
permalink: /debug/
---

<ul>
{% for p in site.pages %}
  <li>{{ p.path }} | {{ p.title }} | {{ p.permalink }} | {{ p.url }}</li>
{% endfor %}
</ul>

{{ site.rrn_taxa | size }}

