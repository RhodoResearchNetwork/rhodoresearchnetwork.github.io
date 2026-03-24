---
layout: default
title: Rhododendron Classification
---

Collections loaded: {{ site.collections | map: "label" }}
Files in /taxa/: {{ site.static_files | where_exp: "f", "f.path contains '/taxa/'" | size }}
<p>Taxa count: {{ site.taxa | size }}</p>

# Rhododendron Classification

This section provides an overview and data related to the Rhododendron classification used by the R‑RN project.

## Species List

{% assign sorted = site.taxa | sort: "title" %}
<ul>
{% for taxon in sorted %}
  <li><a href="{{ taxon.url }}">{{ taxon.title }}</a></li>
{% endfor %}
</ul>

