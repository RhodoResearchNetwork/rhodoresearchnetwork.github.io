---
layout: default
title: Rhododendron Classification
---

# Rhododendron Classification

This section provides an overview and data related species in the Rhododendron classification used by the R‑RN project.
The source for the inital 822 species pages was the [Edinburgh Rhododendron Monographs – Royal Botanic Garden Edinburgh](https://data.rbge.org.uk/service/factsheets/Edinburgh_Rhododendron_Monographs.xhtml). Names have been check agaisnt the WFO and IPNI to updated nomenclature. Additional species pages and infraspcific taxa will be added.

## Species List

{% assign rrn_taxa = site.rrn_taxa | default: empty %}
{% if rrn_taxa != empty %}
  {% assign sorted = rrn_taxa | sort: "title" %}
  <ul>
  {% for t in sorted %}
    <li><a href="{{ t.url }}">{{ t.title }}</a></li>
  {% endfor %}
  </ul>
{% else %}
  <p>No taxa found.</p>
{% endif %}
