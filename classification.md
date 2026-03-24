---
layout: default
title: Rhododendron Classification
---



# Rhododendron Classification

This section provides an overview and data related to the Rhododendron classification used by the R‑RN project.

## Species List

- [Rhododendron aberconwayi](rrn-taxa/rhododendron_aberconwayi.md)

{% assign rrn_taxa = site.rrn_taxa | default: empty %}
{% if rrn_taxa != empty %}
  {% assign sorted = rrn_taxa | sort: "title" %}
  {% for t in sorted %}
    {{ t.title }}
  {% endfor %}
{% else %}
  <p>No taxa found.</p>
{% endif %}

<h3>Collections loaded:</h3>
{{ site.collections | map: "label" | join: ", " }}

<h3>rrn_taxa count:</h3>
{{ site.rrn_taxa | size }}

<h3>rrn_taxa items:</h3>
<ul>
{% for item in site.rrn_taxa %}
  <li>{{ item.path }}</li>
{% endfor %}
</ul>
