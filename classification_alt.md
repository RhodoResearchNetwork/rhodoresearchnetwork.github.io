---
layout: default
title: Rhododendron Classification
---

# Rhododendron Classification

This section provides an overview and data related species in the Rhododendron classification used by the R‑RN project.
The source for the inital 822 species pages was the [Edinburgh Rhododendron Monographs – Royal Botanic Garden Edinburgh](https://data.rbge.org.uk/service/factsheets/Edinburgh_Rhododendron_Monographs.xhtml). Names have been check against the WFO and IPNI to updated nomenclature. Additional species pages and infraspcific taxa will be added.

## Species List
{% assign rrn_taxa = site.rrn_taxa | default: empty %}
{% if rrn_taxa != empty %}
  {% assign sorted = rrn_taxa 
      | sort: "title"
      | sort: "subsection"
      | sort: "section"
      | sort: "subgenus"
  %}
{% endif %}

{% assign current_subgenus = "" %}
{% assign current_section = "" %}
{% assign current_subsection = "" %}

{% for t in sorted %}

{% if t.subgenus and t.subgenus != current_subgenus %}
<h2>subg. {{ t.subgenus }}</h2>
{% assign current_subgenus = t.subgenus %}
{% assign current_section = "" %}
{% assign current_subsection = "" %}
{% endif %}

{% if t.section and t.section != current_section %}
<h3>sect. {{ t.section }}</h3>
{% assign current_section = t.section %}
{% assign current_subsection = "" %}
{% endif %}

{% if t.subsection and t.subsection != current_subsection %}
<h4>subsect. {{ t.subsection }}</h4>
{% assign current_subsection = t.subsection %}
{% endif %}

<p><a href="{{ t.url }}">{{ t.title }}</a></p>

{% endfor %}