---
layout: default
title: Rhododendron Classification
---

<p>Taxa count: {{ site.taxa | size }}</p>
<p>Collections loaded: {{ site.collections | map: "label" }}</p>
<p>Root contains taxa folder: {{ site.static_files | where_exp: "f", "f.path contains 'taxa/'" | size }}</p>

# Rhododendron Classification

This section provides an overview and data related to the Rhododendron classification used by the R‑RN project.

## Species List

- [Rhododendron aberconway](taxa/rhododendron_aberconwayi.md)

{% assign sorted = site.taxa | sort: "title" %}
<ul>
{% for taxon in sorted %}
  <li><a href="{{ taxon.url }}">{{ taxon.title }}</a></li>
{% endfor %}
</ul>

