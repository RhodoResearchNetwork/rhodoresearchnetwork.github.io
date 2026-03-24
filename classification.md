---
layout: default
title: Rhododendron Classification
---

# Rhododendron Classification

This section provides an overview and data related to the Rhododendron classification used by the R‑RN project.

## Species List

{% assign sorted = site.taxa | sort: "title" %}
<ul>
{% for taxon in sorted %}
  <li><a href="{{ taxon.url }}">{{ taxon.title }}</a></li>
{% endfor %}
</ul>

<p>Taxa count: {{ site.taxa | size }}</p>