---
layout: default
title: Rhododendron Classification
---

<p>Collections loaded: {{ site.collections | map: "label" }}</p>
<p>rrn_taxa count: {{ site.rrn_taxa | size }}</p>
<p>Root contains rrn_taxa folder: {{ site.static_files | where_exp: "f", "f.path contains 'rrn_taxa/'" | size }}</p>

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

