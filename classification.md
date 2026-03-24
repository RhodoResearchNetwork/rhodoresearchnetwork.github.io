---
layout: default
title: Rhododendron Classification
---

<p>Collections loaded: {{ site.collections | map: "label" }}</p>
<p>Site source: {{ site.source }}</p>
<p>Files in /taxa/: {{ site.static_files | where: "path", "/taxa" | size }}</p>

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