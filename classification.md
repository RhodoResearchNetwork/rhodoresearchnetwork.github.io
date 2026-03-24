---
layout: default
title: Rhododendron Classification
---

# Rhododendron Classification

This section provides an overview of the Rhododendron classification used by the R‑RN project.

## Species List

{% assign by_subgenus = site.taxa | group_by: "subfamily" %}
{% for subgenus in by_subgenus %}
## {{ subgenus.name }}

  {% assign by_section = subgenus.items | group_by: "section" %}
  {% for section in by_section %}
  ### {{ section.name }}

    <ul>
    {% for taxon in section.items %}
      <li><a href="{{ taxon.url }}">{{ taxon.title }}</a></li>
    {% endfor %}
    </ul>

  {% endfor %}
{% endfor %}