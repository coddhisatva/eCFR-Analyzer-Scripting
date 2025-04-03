TRUNCATE cfr_references CASCADE; INSERT INTO cfr_references (agency_id, title, subheading, ordinal, node_id) SELECT agency_id, title, subheading, ordinal, node_id FROM jsonb_populate_recordset(null::cfr_references, $JSON$[
  {
    "id": 116982534,
    "agency_id": "administrative-conference-of-the-united-states",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=III"
  },
  {
    "id": 1966267750,
    "agency_id": "advisory-council-on-historic-preservation",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=VIII"
  },
  {
    "id": 1754101466,
    "agency_id": "special-inspector-general-for-afghanistan-reconstruction",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXXIII"
  },
  {
    "id": 1299112275,
    "agency_id": "african-development-foundation",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XV"
  },
  {
    "id": 814167095,
    "agency_id": "african-development-foundation",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=57"
  },
  {
    "id": 2028120358,
    "agency_id": "united-states-agency-for-global-media",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=V"
  },
  {
    "id": 1781225424,
    "agency_id": "united-states-agency-for-global-media",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=19"
  },
  {
    "id": 170129043,
    "agency_id": "agriculture-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=IV"
  },
  {
    "id": 1984706276,
    "agency_id": "agriculture-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXIII"
  },
  {
    "id": 99789196,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVI"
  },
  {
    "id": 533311766,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XX"
  },
  {
    "id": 839925076,
    "agency_id": "agriculture-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=4"
  },
  {
    "id": 996020575,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=I"
  },
  {
    "id": 1528629313,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=VIII"
  },
  {
    "id": 1657519520,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=IX"
  },
  {
    "id": 700000519,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=X"
  },
  {
    "id": 433365706,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XI"
  },
  {
    "id": 1395731720,
    "agency_id": "agriculture-department",
    "title": 9,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=9/chapter=II"
  },
  {
    "id": 1232354841,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=V"
  },
  {
    "id": 2938095,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=III"
  },
  {
    "id": 2058727897,
    "agency_id": "agriculture-department",
    "title": 9,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=9/chapter=I"
  },
  {
    "id": 1745591406,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XIV"
  },
  {
    "id": 755736287,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXVII"
  },
  {
    "id": 1791806115,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=VII"
  },
  {
    "id": 249488690,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=IV"
  },
  {
    "id": 141004710,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=II"
  },
  {
    "id": 481425849,
    "agency_id": "agriculture-department",
    "title": 9,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=9/chapter=III"
  },
  {
    "id": 294097446,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XV"
  },
  {
    "id": 1392194906,
    "agency_id": "agriculture-department",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=II"
  },
  {
    "id": 846915317,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXVI"
  },
  {
    "id": 953650801,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXIV"
  },
  {
    "id": 443487664,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=VI"
  },
  {
    "id": 1509979747,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXV"
  },
  {
    "id": 42258683,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXX"
  },
  {
    "id": 1678959617,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXIX"
  },
  {
    "id": 1741210748,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXI"
  },
  {
    "id": 1474674741,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXVII"
  },
  {
    "id": 748019838,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXVI"
  },
  {
    "id": 1829512462,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXVIII"
  },
  {
    "id": 1253163172,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXII"
  },
  {
    "id": 1189771267,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=A"
  },
  {
    "id": 1976055714,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXIII"
  },
  {
    "id": 2007250299,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVIII"
  },
  {
    "id": 649184329,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XLII"
  },
  {
    "id": 40989802,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=L"
  },
  {
    "id": 2007250299,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVIII"
  },
  {
    "id": 518570836,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXV"
  },
  {
    "id": 40989802,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=L"
  },
  {
    "id": 981342880,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVII"
  },
  {
    "id": 2007250299,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVIII"
  },
  {
    "id": 649184329,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XLII"
  },
  {
    "id": 40989802,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=L"
  },
  {
    "id": 1608892394,
    "agency_id": "agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXVIII"
  },
  {
    "id": 1026515197,
    "agency_id": "agricultural-marketing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=I"
  },
  {
    "id": 1907272152,
    "agency_id": "agricultural-marketing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=VIII"
  },
  {
    "id": 1087727802,
    "agency_id": "agricultural-marketing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=IX"
  },
  {
    "id": 66929709,
    "agency_id": "agricultural-marketing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=X"
  },
  {
    "id": 44025633,
    "agency_id": "agricultural-marketing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XI"
  },
  {
    "id": 1414118471,
    "agency_id": "agricultural-marketing-service",
    "title": 9,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=9/chapter=II"
  },
  {
    "id": 2013162918,
    "agency_id": "agricultural-research-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=V"
  },
  {
    "id": 801988438,
    "agency_id": "animal-and-plant-health-inspection-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=III"
  },
  {
    "id": 1023969825,
    "agency_id": "animal-and-plant-health-inspection-service",
    "title": 9,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=9/chapter=I"
  },
  {
    "id": 1083420965,
    "agency_id": "commodity-credit-corporation",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XIV"
  },
  {
    "id": 10328700,
    "agency_id": "economic-research-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXVII"
  },
  {
    "id": 330401673,
    "agency_id": "farm-service-agency",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=VII"
  },
  {
    "id": 258581011,
    "agency_id": "federal-crop-insurance-corporation",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=IV"
  },
  {
    "id": 1403785048,
    "agency_id": "food-and-nutrition-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=II"
  },
  {
    "id": 905402017,
    "agency_id": "food-safety-and-inspection-service",
    "title": 9,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=9/chapter=III"
  },
  {
    "id": 296528936,
    "agency_id": "foreign-agricultural-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XV"
  },
  {
    "id": 164740648,
    "agency_id": "forest-service",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=II"
  },
  {
    "id": 860287947,
    "agency_id": "national-agricultural-statistics-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXVI"
  },
  {
    "id": 2034468059,
    "agency_id": "national-institute-of-food-and-agriculture",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXIV"
  },
  {
    "id": 1360367464,
    "agency_id": "natural-resources-conservation-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=VI"
  },
  {
    "id": 1255509423,
    "agency_id": "advocacy-and-outreach-office",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXV"
  },
  {
    "id": 354725281,
    "agency_id": "office-of-the-chief-financial-officer-agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXX"
  },
  {
    "id": 117865797,
    "agency_id": "energy-policy-and-new-uses-office",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXIX"
  },
  {
    "id": 1700759149,
    "agency_id": "office-of-environmental-quality",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXI"
  },
  {
    "id": 1305716521,
    "agency_id": "office-of-information-resources-management",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXVII"
  },
  {
    "id": 555722330,
    "agency_id": "inspector-general-office-agriculture-department",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXVI"
  },
  {
    "id": 1537936798,
    "agency_id": "office-of-operations",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXVIII"
  },
  {
    "id": 192129424,
    "agency_id": "procurement-and-property-management-office-of",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXII"
  },
  {
    "id": 1383147136,
    "agency_id": "office-of-secretary-of-agriculture",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=A"
  },
  {
    "id": 74905705,
    "agency_id": "transportation-office",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXIII"
  },
  {
    "id": 1836830977,
    "agency_id": "rural-business-cooperative-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVIII"
  },
  {
    "id": 2134246278,
    "agency_id": "rural-business-cooperative-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XLII"
  },
  {
    "id": 446165979,
    "agency_id": "rural-business-cooperative-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=L"
  },
  {
    "id": 682567206,
    "agency_id": "rural-housing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVIII"
  },
  {
    "id": 1294491466,
    "agency_id": "rural-housing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXV"
  },
  {
    "id": 394684934,
    "agency_id": "rural-housing-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=L"
  },
  {
    "id": 1117640524,
    "agency_id": "rural-utilities-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVII"
  },
  {
    "id": 1560939573,
    "agency_id": "rural-utilities-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XVIII"
  },
  {
    "id": 2047161653,
    "agency_id": "rural-utilities-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XLII"
  },
  {
    "id": 692177836,
    "agency_id": "rural-utilities-service",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=L"
  },
  {
    "id": 1799004265,
    "agency_id": "world-agricultural-outlook-board",
    "title": 7,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=7/chapter=XXXVIII"
  },
  {
    "id": 209106793,
    "agency_id": "air-transportation-stabilization-board",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=VI"
  },
  {
    "id": 906434326,
    "agency_id": "american-battle-monuments-commission",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=IV"
  },
  {
    "id": 547946457,
    "agency_id": "appalachian-regional-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=IX"
  },
  {
    "id": 234244646,
    "agency_id": "architectural-and-transportation-barriers-compliance-board",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=XI"
  },
  {
    "id": 2004995661,
    "agency_id": "arctic-research-commission",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XXIII"
  },
  {
    "id": 1324419245,
    "agency_id": "armed-forces-retirement-home",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XI"
  },
  {
    "id": 1984645408,
    "agency_id": "armed-forces-retirement-home",
    "title": 38,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=38/chapter=II"
  },
  {
    "id": 35568968,
    "agency_id": "committee-for-purchase-from-people-who-are-blind-or-severely-disabled",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=51"
  },
  {
    "id": 1013935542,
    "agency_id": "central-intelligence-agency",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XIX"
  },
  {
    "id": 2004176522,
    "agency_id": "chemical-safety-and-hazard-investigation-board",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=VI"
  },
  {
    "id": 56233627,
    "agency_id": "civil-rights-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXVIII"
  },
  {
    "id": 830537341,
    "agency_id": "civil-rights-commission",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=VII"
  },
  {
    "id": 1395679088,
    "agency_id": "commerce-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XIII"
  },
  {
    "id": 1522900694,
    "agency_id": "commerce-department",
    "title": 44,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=44/chapter=IV"
  },
  {
    "id": 654034170,
    "agency_id": "commerce-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=13"
  },
  {
    "id": 1754160336,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=I"
  },
  {
    "id": 240925668,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=VIII"
  },
  {
    "id": 15372822,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=VII"
  },
  {
    "id": 796387518,
    "agency_id": "commerce-department",
    "title": 13,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=13/chapter=III"
  },
  {
    "id": 218685846,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=IV"
  },
  {
    "id": 1672891590,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=III"
  },
  {
    "id": 1276260406,
    "agency_id": "commerce-department",
    "title": 19,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=19/chapter=III"
  },
  {
    "id": 12420108,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XIV"
  },
  {
    "id": 895188222,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=II"
  },
  {
    "id": 337241335,
    "agency_id": "commerce-department",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=IV"
  },
  {
    "id": 2057550495,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=IX"
  },
  {
    "id": 1953234438,
    "agency_id": "commerce-department",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=III"
  },
  {
    "id": 1180342748,
    "agency_id": "commerce-department",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=IV"
  },
  {
    "id": 780904664,
    "agency_id": "commerce-department",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=II"
  },
  {
    "id": 371031984,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XI"
  },
  {
    "id": 1833760322,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XXIII"
  },
  {
    "id": 990791093,
    "agency_id": "commerce-department",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=III"
  },
  {
    "id": 561311330,
    "agency_id": "commerce-department",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=IV"
  },
  {
    "id": 912837134,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=A"
  },
  {
    "id": 92386255,
    "agency_id": "commerce-department",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XV"
  },
  {
    "id": 1193772723,
    "agency_id": "commerce-department",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=I"
  },
  {
    "id": 1944331529,
    "agency_id": "census-bureau",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=I"
  },
  {
    "id": 488870967,
    "agency_id": "economic-analysis-bureau",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=VIII"
  },
  {
    "id": 1001551561,
    "agency_id": "industry-and-security-bureau",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=VII"
  },
  {
    "id": 1737269465,
    "agency_id": "economic-development-administration",
    "title": 13,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=13/chapter=III"
  },
  {
    "id": 722039374,
    "agency_id": "foreign-trade-zones-board",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=IV"
  },
  {
    "id": 877943096,
    "agency_id": "international-trade-administration",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=III"
  },
  {
    "id": 974461094,
    "agency_id": "international-trade-administration",
    "title": 19,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=19/chapter=III"
  },
  {
    "id": 1043410870,
    "agency_id": "minority-business-development-agency",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XIV"
  },
  {
    "id": 411822232,
    "agency_id": "national-institute-of-standards-and-technology",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=II"
  },
  {
    "id": 15998741,
    "agency_id": "national-institute-of-standards-and-technology",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=IV"
  },
  {
    "id": 219266883,
    "agency_id": "national-oceanic-and-atmospheric-administration",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=IX"
  },
  {
    "id": 1258822105,
    "agency_id": "national-oceanic-and-atmospheric-administration",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=III"
  },
  {
    "id": 1965965113,
    "agency_id": "national-oceanic-and-atmospheric-administration",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=IV"
  },
  {
    "id": 1960293897,
    "agency_id": "national-oceanic-and-atmospheric-administration-national-marine-fisheries-service",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=II"
  },
  {
    "id": 1737854685,
    "agency_id": "national-technical-information-service",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XI"
  },
  {
    "id": 463508338,
    "agency_id": "national-telecommunications-and-information-administration",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XXIII"
  },
  {
    "id": 1675623387,
    "agency_id": "national-telecommunications-and-information-administration",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=III"
  },
  {
    "id": 1845885487,
    "agency_id": "national-telecommunications-and-information-administration",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=IV"
  },
  {
    "id": 1135373034,
    "agency_id": "office-of-secretary-of-commerce",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=A"
  },
  {
    "id": 1862962565,
    "agency_id": "under-secretary-for-economic-affairs",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XV"
  },
  {
    "id": 1006317673,
    "agency_id": "patent-and-trademark-office",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=I"
  },
  {
    "id": 501251282,
    "agency_id": "commodity-futures-trading-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLI"
  },
  {
    "id": 393272710,
    "agency_id": "commodity-futures-trading-commission",
    "title": 17,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=17/chapter=I"
  },
  {
    "id": 1633407561,
    "agency_id": "construction-industry-collective-bargaining-commission",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=IX"
  },
  {
    "id": 207488728,
    "agency_id": "consumer-financial-protection-bureau",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXXIV"
  },
  {
    "id": 1373482995,
    "agency_id": "consumer-financial-protection-bureau",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=X"
  },
  {
    "id": 158791872,
    "agency_id": "consumer-product-safety-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXI"
  },
  {
    "id": 1448052090,
    "agency_id": "consumer-product-safety-commission",
    "title": 16,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=16/chapter=II"
  },
  {
    "id": 2081297400,
    "agency_id": "council-of-the-inspectors-general-on-integrity-and-efficiency",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XCVIII"
  },
  {
    "id": 1832078161,
    "agency_id": "court-services-and-offender-supervision-agency-for-the-district-of-columbia",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXX"
  },
  {
    "id": 1732905178,
    "agency_id": "court-services-and-offender-supervision-agency-for-the-district-of-columbia",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=VIII"
  },
  {
    "id": 2049899295,
    "agency_id": "defense-nuclear-facilities-safety-board",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=XVII"
  },
  {
    "id": 865451190,
    "agency_id": "defense-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XI"
  },
  {
    "id": 1611280366,
    "agency_id": "defense-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXVI"
  },
  {
    "id": 2144131715,
    "agency_id": "defense-department",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=A"
  },
  {
    "id": 900948793,
    "agency_id": "defense-department",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=VII"
  },
  {
    "id": 415297737,
    "agency_id": "defense-department",
    "title": 33,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=33/chapter=II"
  },
  {
    "id": 955650747,
    "agency_id": "defense-department",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=III"
  },
  {
    "id": 140504022,
    "agency_id": "defense-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=2"
  },
  {
    "id": 2063804333,
    "agency_id": "defense-department",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XII"
  },
  {
    "id": 475045694,
    "agency_id": "defense-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=54"
  },
  {
    "id": 1292000291,
    "agency_id": "defense-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=52"
  },
  {
    "id": 1998354800,
    "agency_id": "defense-department",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=I"
  },
  {
    "id": 829865663,
    "agency_id": "engineers-corps",
    "title": 33,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=33/chapter=II"
  },
  {
    "id": 1165735188,
    "agency_id": "engineers-corps",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=III"
  },
  {
    "id": 1047225506,
    "agency_id": "defense-acquisition-regulations-system",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=2"
  },
  {
    "id": 1651955161,
    "agency_id": "defense-logistics-agency",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XII"
  },
  {
    "id": 275600726,
    "agency_id": "defense-logistics-agency",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=54"
  },
  {
    "id": 977256567,
    "agency_id": "department-of-navy-acquisition-regulations",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=52"
  },
  {
    "id": 2058679448,
    "agency_id": "office-of-the-secretary",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=I"
  },
  {
    "id": 742752883,
    "agency_id": "delaware-river-basin-commission",
    "title": 18,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=18/chapter=III"
  },
  {
    "id": 388530612,
    "agency_id": "denali-commission",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=IX"
  },
  {
    "id": 1429360653,
    "agency_id": "national-intelligence-office-of-the-national-director",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=IV"
  },
  {
    "id": 1814790965,
    "agency_id": "national-intelligence-office-of-the-national-director",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XVII"
  },
  {
    "id": 814917560,
    "agency_id": "national-council-on-disability",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=C"
  },
  {
    "id": 972825546,
    "agency_id": "national-council-on-disability",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=XII"
  },
  {
    "id": 1878055548,
    "agency_id": "east-west-foreign-trade-board",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XIII"
  },
  {
    "id": 1584047335,
    "agency_id": "education-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXIV"
  },
  {
    "id": 837811136,
    "agency_id": "education-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LIII"
  },
  {
    "id": 1208481776,
    "agency_id": "education-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=34"
  },
  {
    "id": 62728485,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=I"
  },
  {
    "id": 663350298,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=IV"
  },
  {
    "id": 940882685,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=V"
  },
  {
    "id": 440755313,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=II"
  },
  {
    "id": 1960707031,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=VI"
  },
  {
    "id": 1355202827,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=A"
  },
  {
    "id": 2058536753,
    "agency_id": "education-department",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=III"
  },
  {
    "id": 1904616011,
    "agency_id": "department-of-education-acquisition-regulation",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=34"
  },
  {
    "id": 1126356975,
    "agency_id": "office-for-civil-rights",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=I"
  },
  {
    "id": 1690741542,
    "agency_id": "office-of-and-adult-education-technical-career",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=IV"
  },
  {
    "id": 709158597,
    "agency_id": "office-of-bilingual-education-and-minority-languages-affairs",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=V"
  },
  {
    "id": 1994128560,
    "agency_id": "office-of-elementary-and-secondary-education",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=II"
  },
  {
    "id": 1097929066,
    "agency_id": "office-of-postsecondary-education",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=VI"
  },
  {
    "id": 281582835,
    "agency_id": "office-of-secretary-of-education",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=A"
  },
  {
    "id": 80814150,
    "agency_id": "office-of-special-education-and-rehabilitative-services",
    "title": 34,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=34/chapter=III"
  },
  {
    "id": 1545510108,
    "agency_id": "election-assistance-commission",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=LVIII"
  },
  {
    "id": 1637171783,
    "agency_id": "election-assistance-commission",
    "title": 11,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=11/chapter=II"
  },
  {
    "id": 1428836169,
    "agency_id": "emergency-oil-and-gas-guaranteed-loan-board",
    "title": 13,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=13/chapter=V"
  },
  {
    "id": 815780779,
    "agency_id": "emergency-steel-guarantee-loan-board",
    "title": 13,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=13/chapter=IV"
  },
  {
    "id": 768185667,
    "agency_id": "national-commission-for-employment-policy",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=IV"
  },
  {
    "id": 768372310,
    "agency_id": "energy-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=IX"
  },
  {
    "id": 600566996,
    "agency_id": "energy-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXIII"
  },
  {
    "id": 1509903450,
    "agency_id": "energy-department",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=II"
  },
  {
    "id": 95259573,
    "agency_id": "energy-department",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=III"
  },
  {
    "id": 1436452350,
    "agency_id": "energy-department",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=X"
  },
  {
    "id": 1065412957,
    "agency_id": "energy-department",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=109"
  },
  {
    "id": 2079208292,
    "agency_id": "energy-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=9"
  },
  {
    "id": 1008788808,
    "agency_id": "energy-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXIV"
  },
  {
    "id": 179306225,
    "agency_id": "energy-department",
    "title": 18,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=18/chapter=I"
  },
  {
    "id": 187197356,
    "agency_id": "federal-energy-regulatory-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXIV"
  },
  {
    "id": 264331064,
    "agency_id": "federal-energy-regulatory-commission",
    "title": 18,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=18/chapter=I"
  },
  {
    "id": 1653224730,
    "agency_id": "joint-board-for-enrollment-of-actuaries",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=VIII"
  },
  {
    "id": 1132390932,
    "agency_id": "environmental-protection-agency",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XV"
  },
  {
    "id": 777942686,
    "agency_id": "environmental-protection-agency",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LIV"
  },
  {
    "id": 1750437320,
    "agency_id": "environmental-protection-agency",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=I"
  },
  {
    "id": 917021789,
    "agency_id": "environmental-protection-agency",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=IV"
  },
  {
    "id": 1831803956,
    "agency_id": "environmental-protection-agency",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=VII"
  },
  {
    "id": 411123533,
    "agency_id": "environmental-protection-agency",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=115"
  },
  {
    "id": 1144166674,
    "agency_id": "environmental-protection-agency",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=15"
  },
  {
    "id": 1850152609,
    "agency_id": "equal-employment-opportunity-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXII"
  },
  {
    "id": 1018293338,
    "agency_id": "equal-employment-opportunity-commission",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XIV"
  },
  {
    "id": 1931843403,
    "agency_id": "executive-office-of-the-president",
    "title": 3,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=3/chapter=I"
  },
  {
    "id": 726496602,
    "agency_id": "executive-office-of-the-president",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=V"
  },
  {
    "id": 150836353,
    "agency_id": "executive-office-of-the-president",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XXI"
  },
  {
    "id": 2060127626,
    "agency_id": "executive-office-of-the-president",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=II"
  },
  {
    "id": 1922627833,
    "agency_id": "executive-office-of-the-president",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XXIV"
  },
  {
    "id": 2060127626,
    "agency_id": "executive-office-of-the-president",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=II"
  },
  {
    "id": 160268193,
    "agency_id": "executive-office-of-the-president",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=CIV"
  },
  {
    "id": 1525095559,
    "agency_id": "council-on-environmental-quality",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=V"
  },
  {
    "id": 1567440726,
    "agency_id": "national-security-council",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XXI"
  },
  {
    "id": 489885165,
    "agency_id": "national-security-council",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=II"
  },
  {
    "id": 572723880,
    "agency_id": "science-and-technology-policy-office",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XXIV"
  },
  {
    "id": 1852325157,
    "agency_id": "science-and-technology-policy-office",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=II"
  },
  {
    "id": 41323357,
    "agency_id": "office-of-the-intellectual-property-enforcement-coordinator",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=CIV"
  },
  {
    "id": 942154698,
    "agency_id": "export-import-bank",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXV"
  },
  {
    "id": 1293715226,
    "agency_id": "export-import-bank",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LII"
  },
  {
    "id": 1248408538,
    "agency_id": "export-import-bank",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=IV"
  },
  {
    "id": 762217643,
    "agency_id": "farm-credit-administration",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXXI"
  },
  {
    "id": 1473655081,
    "agency_id": "farm-credit-administration",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=VI"
  },
  {
    "id": 1701352386,
    "agency_id": "farm-credit-system-insurance-corporation",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXX"
  },
  {
    "id": 385500371,
    "agency_id": "farm-credit-system-insurance-corporation",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XIV"
  },
  {
    "id": 835099374,
    "agency_id": "federal-acquisition-regulation",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=1"
  },
  {
    "id": 1066166027,
    "agency_id": "federal-acqusition-supply-chain-security",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=201"
  },
  {
    "id": 1760694120,
    "agency_id": "federal-communications-commission",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=LX"
  },
  {
    "id": 1607055387,
    "agency_id": "federal-communications-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXIX"
  },
  {
    "id": 1991570840,
    "agency_id": "federal-communications-commission",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=I"
  },
  {
    "id": 2068637800,
    "agency_id": "federal-deposit-insurance-corporation",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXII"
  },
  {
    "id": 387950909,
    "agency_id": "federal-deposit-insurance-corporation",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=III"
  },
  {
    "id": 1106209329,
    "agency_id": "federal-election-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXXVII"
  },
  {
    "id": 934124583,
    "agency_id": "federal-election-commission",
    "title": 11,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=11/chapter=I"
  },
  {
    "id": 458921338,
    "agency_id": "federal-financial-institutions-examination-council",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XI"
  },
  {
    "id": 1714652482,
    "agency_id": "federal-financing-bank",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=VIII"
  },
  {
    "id": 250942407,
    "agency_id": "federal-housing-finance-agency",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXX"
  },
  {
    "id": 916190216,
    "agency_id": "federal-housing-finance-agency",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XII"
  },
  {
    "id": 583165028,
    "agency_id": "federal-labor-relations-authority",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLIX"
  },
  {
    "id": 1683176200,
    "agency_id": "federal-labor-relations-authority",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 1052275712,
    "agency_id": "federal-labor-relations-authority",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XIV"
  },
  {
    "id": 1052275712,
    "agency_id": "federal-labor-relations-authority",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XIV"
  },
  {
    "id": 1683176200,
    "agency_id": "federal-labor-relations-authority",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 1803485809,
    "agency_id": "federal-service-impasses-panel",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XIV"
  },
  {
    "id": 1578388049,
    "agency_id": "general-counsel-of-the-federal-labor-relations-authority",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XIV"
  },
  {
    "id": 1583907119,
    "agency_id": "general-counsel-of-the-federal-labor-relations-authority",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 400000157,
    "agency_id": "federal-maritime-commission",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=IV"
  },
  {
    "id": 184738035,
    "agency_id": "federal-mediation-and-conciliation-service",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=CIII"
  },
  {
    "id": 175329692,
    "agency_id": "federal-mediation-and-conciliation-service",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XII"
  },
  {
    "id": 624792187,
    "agency_id": "federal-mine-safety-and-health-review-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXIV"
  },
  {
    "id": 1584158025,
    "agency_id": "federal-mine-safety-and-health-review-commission",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XXVII"
  },
  {
    "id": 638593272,
    "agency_id": "federal-permitting-improvement-steering-council",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=IX"
  },
  {
    "id": 1876913655,
    "agency_id": "federal-procurement-regulations-system",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=A"
  },
  {
    "id": 1207231224,
    "agency_id": "federal-property-management-regulations-system",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=C"
  },
  {
    "id": 1764962810,
    "agency_id": "federal-register-administrative-committee",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=I"
  },
  {
    "id": 285202820,
    "agency_id": "federal-reserve-system",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=II"
  },
  {
    "id": 1754063413,
    "agency_id": "federal-reserve-system",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LVIII"
  },
  {
    "id": 2018472352,
    "agency_id": "board-of-governors-of-the-federal-reserve-system",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LVIII"
  },
  {
    "id": 362191228,
    "agency_id": "federal-retirement-thrift-investment-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=VI"
  },
  {
    "id": 1965394840,
    "agency_id": "federal-retirement-thrift-investment-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXVI"
  },
  {
    "id": 1810923118,
    "agency_id": "federal-trade-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLVII"
  },
  {
    "id": 1212166336,
    "agency_id": "federal-trade-commission",
    "title": 16,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=16/chapter=I"
  },
  {
    "id": 2001958128,
    "agency_id": "federal-travel-regulation-system",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=F"
  },
  {
    "id": 816921356,
    "agency_id": "financial-stability-oversight-council",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XIII"
  },
  {
    "id": 559772978,
    "agency_id": "commission-of-fine-arts",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XXI"
  },
  {
    "id": 2044293097,
    "agency_id": "first-responder-network-authority",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=V"
  },
  {
    "id": 1061572908,
    "agency_id": "foreign-service-grievance-board",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=IX"
  },
  {
    "id": 1202329712,
    "agency_id": "foreign-service-impasse-disputes-panel",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 1202329712,
    "agency_id": "foreign-service-impasse-disputes-panel",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 1965867454,
    "agency_id": "foreign-service-labor-relations-board",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 1965867454,
    "agency_id": "foreign-service-labor-relations-board",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIV"
  },
  {
    "id": 505259214,
    "agency_id": "general-services-administration",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LVII"
  },
  {
    "id": 1604004443,
    "agency_id": "general-services-administration",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=105"
  },
  {
    "id": 1111160789,
    "agency_id": "general-services-administration",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=5"
  },
  {
    "id": 1116465159,
    "agency_id": "general-services-administration",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=61"
  },
  {
    "id": 2114962174,
    "agency_id": "civilian-board-of-contract-appeals",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=61"
  },
  {
    "id": 1768748989,
    "agency_id": "government-accountability-office",
    "title": 4,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=4/chapter=I"
  },
  {
    "id": 290719216,
    "agency_id": "government-ethics-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XVI"
  },
  {
    "id": 1975835852,
    "agency_id": "gulf-coast-ecosystem-restoration-council",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=LIX"
  },
  {
    "id": 249612232,
    "agency_id": "gulf-coast-ecosystem-restoration-council",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=VIII"
  },
  {
    "id": 665334213,
    "agency_id": "harry-s-truman-scholarship-foundation",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XVIII"
  },
  {
    "id": 1203748478,
    "agency_id": "health-and-human-services-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=III"
  },
  {
    "id": 1682148477,
    "agency_id": "health-and-human-services-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLV"
  },
  {
    "id": 24854438,
    "agency_id": "health-and-human-services-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=A"
  },
  {
    "id": 1768979469,
    "agency_id": "health-and-human-services-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=3"
  },
  {
    "id": 987804866,
    "agency_id": "health-and-human-services-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XIII"
  },
  {
    "id": 1340761464,
    "agency_id": "health-and-human-services-department",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=IV"
  },
  {
    "id": 1314920092,
    "agency_id": "health-and-human-services-department",
    "title": 21,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=21/chapter=I"
  },
  {
    "id": 1053544432,
    "agency_id": "health-and-human-services-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=V"
  },
  {
    "id": 936231591,
    "agency_id": "health-and-human-services-department",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=I"
  },
  {
    "id": 128578653,
    "agency_id": "health-and-human-services-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=III"
  },
  {
    "id": 1783061326,
    "agency_id": "health-and-human-services-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=X"
  },
  {
    "id": 1323614556,
    "agency_id": "health-and-human-services-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=II"
  },
  {
    "id": 552427508,
    "agency_id": "health-and-human-services-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=IV"
  },
  {
    "id": 13739840,
    "agency_id": "health-and-human-services-department",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=V"
  },
  {
    "id": 936231591,
    "agency_id": "health-and-human-services-department",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=I"
  },
  {
    "id": 343662428,
    "agency_id": "children-and-families-administration",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XIII"
  },
  {
    "id": 1107768704,
    "agency_id": "centers-for-medicare-medicaid-services",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=IV"
  },
  {
    "id": 93005041,
    "agency_id": "food-and-drug-administration",
    "title": 21,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=21/chapter=I"
  },
  {
    "id": 892219815,
    "agency_id": "indian-health-service",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=V"
  },
  {
    "id": 1710302193,
    "agency_id": "indian-health-service",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=I"
  },
  {
    "id": 810026383,
    "agency_id": "office-of-administration-for-children-and-families-child-support-enforcement-(child-support-enforcement-program)",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=III"
  },
  {
    "id": 1136374843,
    "agency_id": "office-of-administration-for-children-and-families-community-services",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=X"
  },
  {
    "id": 1136104284,
    "agency_id": "office-of-administration-for-children-and-families-family-assistance-(assistance-programs)",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=II"
  },
  {
    "id": 407073932,
    "agency_id": "refugee-resettlement-office",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=IV"
  },
  {
    "id": 266401923,
    "agency_id": "office-of-inspector-general-health-care",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=V"
  },
  {
    "id": 978640170,
    "agency_id": "public-health-service",
    "title": 42,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=42/chapter=I"
  },
  {
    "id": 1620520610,
    "agency_id": "homeland-security-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXX"
  },
  {
    "id": 936727179,
    "agency_id": "homeland-security-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXXVI"
  },
  {
    "id": 1546868332,
    "agency_id": "homeland-security-department",
    "title": 8,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=8/chapter=I"
  },
  {
    "id": 419911042,
    "agency_id": "homeland-security-department",
    "title": 33,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=33/chapter=I"
  },
  {
    "id": 639994312,
    "agency_id": "homeland-security-department",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=I"
  },
  {
    "id": 1464875665,
    "agency_id": "homeland-security-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=IV"
  },
  {
    "id": 506479519,
    "agency_id": "homeland-security-department",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=III"
  },
  {
    "id": 1113422109,
    "agency_id": "homeland-security-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=30"
  },
  {
    "id": 252164246,
    "agency_id": "homeland-security-department",
    "title": 44,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=44/chapter=I"
  },
  {
    "id": 424459371,
    "agency_id": "homeland-security-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=VII"
  },
  {
    "id": 1844392736,
    "agency_id": "homeland-security-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XCVII"
  },
  {
    "id": 348592535,
    "agency_id": "homeland-security-department",
    "title": 6,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=6/chapter=I"
  },
  {
    "id": 928279457,
    "agency_id": "homeland-security-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=IV"
  },
  {
    "id": 1756580277,
    "agency_id": "homeland-security-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=XII"
  },
  {
    "id": 683778833,
    "agency_id": "homeland-security-department",
    "title": 19,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=19/chapter=I"
  },
  {
    "id": 179923237,
    "agency_id": "coast-guard",
    "title": 33,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=33/chapter=I"
  },
  {
    "id": 2010588659,
    "agency_id": "coast-guard",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=I"
  },
  {
    "id": 871198247,
    "agency_id": "coast-guard",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=IV"
  },
  {
    "id": 1892402225,
    "agency_id": "coast-guard-(great-lakes-pilotage)",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=III"
  },
  {
    "id": 1530810307,
    "agency_id": "department-of-homeland-security-acquisition-regulation",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=30"
  },
  {
    "id": 913074727,
    "agency_id": "federal-emergency-management-agency",
    "title": 44,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=44/chapter=I"
  },
  {
    "id": 1523914792,
    "agency_id": "federal-law-enforcement-training-center",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=VII"
  },
  {
    "id": 1830678642,
    "agency_id": "human-resources-management-system-(homeland-security---office-of-personnel-management)",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XCVII"
  },
  {
    "id": 1240457646,
    "agency_id": "office-of-the-secretary-of-homeland-security",
    "title": 6,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=6/chapter=I"
  },
  {
    "id": 1108997522,
    "agency_id": "secret-service",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=IV"
  },
  {
    "id": 1646578085,
    "agency_id": "transportation-security-administration",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=XII"
  },
  {
    "id": 585556718,
    "agency_id": "u-s-customs-and-border-protection",
    "title": 19,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=19/chapter=I"
  },
  {
    "id": 633442773,
    "agency_id": "housing-and-urban-development-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXIV"
  },
  {
    "id": 931403059,
    "agency_id": "housing-and-urban-development-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXV"
  },
  {
    "id": 1127220189,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=XV"
  },
  {
    "id": 1693766071,
    "agency_id": "housing-and-urban-development-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=24"
  },
  {
    "id": 1221356662,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=III"
  },
  {
    "id": 200023842,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=V"
  },
  {
    "id": 375905893,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=I"
  },
  {
    "id": 1761901295,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=II"
  },
  {
    "id": 789670527,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=VIII"
  },
  {
    "id": 925144304,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=XX"
  },
  {
    "id": 194426305,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=IX"
  },
  {
    "id": 1436941801,
    "agency_id": "housing-and-urban-development-department",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XVII"
  },
  {
    "id": 205846629,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=IV"
  },
  {
    "id": 1813225936,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=XII"
  },
  {
    "id": 816297885,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=A"
  },
  {
    "id": 73738064,
    "agency_id": "housing-and-urban-development-department",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=VII"
  },
  {
    "id": 889711940,
    "agency_id": "government-national-mortgage-association",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=III"
  },
  {
    "id": 340988747,
    "agency_id": "office-of-assistant-secretary-for-community-planning-and-development",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=V"
  },
  {
    "id": 2106543390,
    "agency_id": "office-of-assistant-secretary-for-equal-opportunity",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=I"
  },
  {
    "id": 1223210919,
    "agency_id": "office-of-assistant-secretary-for-housing---federal-housing-commissioner",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=II"
  },
  {
    "id": 1667649346,
    "agency_id": "office-of-assistant-secretary-for-housing---federal-housing-commissioner",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=VIII"
  },
  {
    "id": 1483702341,
    "agency_id": "office-of-assistant-secretary-for-housing---federal-housing-commissioner",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=XX"
  },
  {
    "id": 1718677096,
    "agency_id": "office-of-assistant-secretary-for-public-and-indian-housing",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=IX"
  },
  {
    "id": 1671559785,
    "agency_id": "office-of-federal-housing-enterprise-oversight",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XVII"
  },
  {
    "id": 1557684704,
    "agency_id": "office-of-housing-and-multifamily-housing-assistance-restructuring",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=IV"
  },
  {
    "id": 1866205004,
    "agency_id": "office-of-inspector-general,-housing-and-urban-development",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=XII"
  },
  {
    "id": 701333171,
    "agency_id": "office-of-secretary",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=A"
  },
  {
    "id": 730327400,
    "agency_id": "office-of-secretary-(housing-assistance-programs-and-public-and-indian-housing-programs)",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=VII"
  },
  {
    "id": 941870494,
    "agency_id": "office-of-independent-counsel",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=VII"
  },
  {
    "id": 949069278,
    "agency_id": "united-states-institute-of-peace",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XVII"
  },
  {
    "id": 405803400,
    "agency_id": "inter-american-foundation",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXIII"
  },
  {
    "id": 2130203040,
    "agency_id": "inter-american-foundation",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=X"
  },
  {
    "id": 1349956438,
    "agency_id": "interior-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XIV"
  },
  {
    "id": 1951323915,
    "agency_id": "interior-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXV"
  },
  {
    "id": 361223023,
    "agency_id": "interior-department",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=114"
  },
  {
    "id": 709319319,
    "agency_id": "interior-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=14"
  },
  {
    "id": 653583444,
    "agency_id": "interior-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=I"
  },
  {
    "id": 1771859062,
    "agency_id": "interior-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=V"
  },
  {
    "id": 1423486821,
    "agency_id": "interior-department",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=II"
  },
  {
    "id": 1571697853,
    "agency_id": "interior-department",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=V"
  },
  {
    "id": 1266553439,
    "agency_id": "interior-department",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=I"
  },
  {
    "id": 750379538,
    "agency_id": "interior-department",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=II"
  },
  {
    "id": 1539829371,
    "agency_id": "interior-department",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=IV"
  },
  {
    "id": 768480387,
    "agency_id": "interior-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=II"
  },
  {
    "id": 1546419736,
    "agency_id": "interior-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=III"
  },
  {
    "id": 893801204,
    "agency_id": "interior-department",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=I"
  },
  {
    "id": 485501349,
    "agency_id": "interior-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=VI"
  },
  {
    "id": 1103148916,
    "agency_id": "interior-department",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=XII"
  },
  {
    "id": 531489222,
    "agency_id": "interior-department",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=A"
  },
  {
    "id": 62552734,
    "agency_id": "interior-department",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=VII"
  },
  {
    "id": 663019275,
    "agency_id": "interior-department",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=VII"
  },
  {
    "id": 1270832401,
    "agency_id": "interior-department",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=I"
  },
  {
    "id": 187596985,
    "agency_id": "interior-department",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=IV"
  },
  {
    "id": 1227263177,
    "agency_id": "interior-department",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=VI"
  },
  {
    "id": 1489151583,
    "agency_id": "indian-affairs-bureau",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=I"
  },
  {
    "id": 1987395445,
    "agency_id": "indian-affairs-bureau",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=V"
  },
  {
    "id": 1878024707,
    "agency_id": "land-management-bureau",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=II"
  },
  {
    "id": 485960720,
    "agency_id": "ocean-energy-management-bureau",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=V"
  },
  {
    "id": 1257032801,
    "agency_id": "reclamation-bureau",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=I"
  },
  {
    "id": 1681646627,
    "agency_id": "safety-and-environmental-enforcement-bureau",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=II"
  },
  {
    "id": 1465680439,
    "agency_id": "geological-survey",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=IV"
  },
  {
    "id": 276302001,
    "agency_id": "indian-arts-and-crafts-board",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=II"
  },
  {
    "id": 1911163432,
    "agency_id": "national-indian-gaming-commission",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=III"
  },
  {
    "id": 812790172,
    "agency_id": "national-park-service",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=I"
  },
  {
    "id": 332266631,
    "agency_id": "office-of-indian-affairs-assistant-secretary",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=VI"
  },
  {
    "id": 838996239,
    "agency_id": "natural-resources-revenue-office",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=XII"
  },
  {
    "id": 1642422939,
    "agency_id": "office-of-secretary-of-the-interior",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=A"
  },
  {
    "id": 523343427,
    "agency_id": "special-trustee-for-american-indians-office",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=VII"
  },
  {
    "id": 545709564,
    "agency_id": "surface-mining-reclamation-and-enforcement-office",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=VII"
  },
  {
    "id": 341032131,
    "agency_id": "fish-and-wildlife-service",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=I"
  },
  {
    "id": 924691683,
    "agency_id": "fish-and-wildlife-service",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=IV"
  },
  {
    "id": 2139827856,
    "agency_id": "fish-and-wildlife-service",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=VI"
  },
  {
    "id": 1498264779,
    "agency_id": "international-boundary-and-water-commission-united-states-and-mexico",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XI"
  },
  {
    "id": 1013265279,
    "agency_id": "united-states-international-development-cooperation-agency",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XII"
  },
  {
    "id": 1490171899,
    "agency_id": "u-s-international-development-finance-corporation",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XVI"
  },
  {
    "id": 2118469808,
    "agency_id": "u-s-international-development-finance-corporation",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXXIII"
  },
  {
    "id": 1038379795,
    "agency_id": "u-s-international-development-finance-corporation",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=VII"
  },
  {
    "id": 620288614,
    "agency_id": "agency-for-international-development",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=VII"
  },
  {
    "id": 139755684,
    "agency_id": "agency-for-international-development",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=II"
  },
  {
    "id": 1045625175,
    "agency_id": "agency-for-international-development",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=7"
  },
  {
    "id": 1553813115,
    "agency_id": "international-joint-commission-united-states-and-canada",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=IV"
  },
  {
    "id": 283372380,
    "agency_id": "international-organizations-employees-loyalty-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=V"
  },
  {
    "id": 2076153737,
    "agency_id": "international-trade-commission",
    "title": 19,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=19/chapter=II"
  },
  {
    "id": 1669532632,
    "agency_id": "interstate-commerce-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XL"
  },
  {
    "id": 1261496042,
    "agency_id": "james-madison-memorial-fellowship-foundation",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XXIV"
  },
  {
    "id": 418158947,
    "agency_id": "japan-united-states-friendship-commission",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XVI"
  },
  {
    "id": 781716995,
    "agency_id": "justice-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXVIII"
  },
  {
    "id": 69865216,
    "agency_id": "justice-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXVIII"
  },
  {
    "id": 169550421,
    "agency_id": "justice-department",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=I"
  },
  {
    "id": 1211273318,
    "agency_id": "justice-department",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=XI"
  },
  {
    "id": 2122292333,
    "agency_id": "justice-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=IX"
  },
  {
    "id": 1832265346,
    "agency_id": "justice-department",
    "title": 40,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=40/chapter=IV"
  },
  {
    "id": 1042381586,
    "agency_id": "justice-department",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=128"
  },
  {
    "id": 776070888,
    "agency_id": "justice-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=28"
  },
  {
    "id": 1635650245,
    "agency_id": "justice-department",
    "title": 27,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=27/chapter=II"
  },
  {
    "id": 217263882,
    "agency_id": "justice-department",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=V"
  },
  {
    "id": 55375961,
    "agency_id": "justice-department",
    "title": 21,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=21/chapter=II"
  },
  {
    "id": 1216917341,
    "agency_id": "justice-department",
    "title": 8,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=8/chapter=V"
  },
  {
    "id": 1627446496,
    "agency_id": "justice-department",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=III"
  },
  {
    "id": 366912344,
    "agency_id": "justice-department",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=V"
  },
  {
    "id": 1212453269,
    "agency_id": "justice-department",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=VI"
  },
  {
    "id": 1209757935,
    "agency_id": "alcohol-tobacco-firearms-and-explosives-bureau",
    "title": 27,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=27/chapter=II"
  },
  {
    "id": 382469377,
    "agency_id": "prisons-bureau",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=V"
  },
  {
    "id": 378560079,
    "agency_id": "drug-enforcement-administration",
    "title": 21,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=21/chapter=II"
  },
  {
    "id": 1521615871,
    "agency_id": "executive-office-for-immigration-review",
    "title": 8,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=8/chapter=V"
  },
  {
    "id": 1191104602,
    "agency_id": "federal-prison-industries",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=III"
  },
  {
    "id": 226523465,
    "agency_id": "foreign-claims-settlement-commission",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=V"
  },
  {
    "id": 576370179,
    "agency_id": "offices-of-independent-counsel",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=VI"
  },
  {
    "id": 1011880711,
    "agency_id": "labor-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXIX"
  },
  {
    "id": 1294492541,
    "agency_id": "labor-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLII"
  },
  {
    "id": 430551891,
    "agency_id": "labor-department",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=50"
  },
  {
    "id": 648662086,
    "agency_id": "labor-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=29"
  },
  {
    "id": 105886816,
    "agency_id": "labor-department",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=VII"
  },
  {
    "id": 1348237330,
    "agency_id": "labor-department",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XXV"
  },
  {
    "id": 1371576966,
    "agency_id": "labor-department",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=IV"
  },
  {
    "id": 1432411284,
    "agency_id": "labor-department",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=V"
  },
  {
    "id": 1785836318,
    "agency_id": "labor-department",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=I"
  },
  {
    "id": 1007439462,
    "agency_id": "labor-department",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XVII"
  },
  {
    "id": 1250293462,
    "agency_id": "labor-department",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=IX"
  },
  {
    "id": 1184366140,
    "agency_id": "labor-department",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=61"
  },
  {
    "id": 198302981,
    "agency_id": "labor-department",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=60"
  },
  {
    "id": 276490560,
    "agency_id": "labor-department",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=II"
  },
  {
    "id": 2110384479,
    "agency_id": "labor-department",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=IV"
  },
  {
    "id": 1961668513,
    "agency_id": "labor-department",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=A"
  },
  {
    "id": 741804765,
    "agency_id": "labor-department",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=I"
  },
  {
    "id": 77050057,
    "agency_id": "labor-department",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=VI"
  },
  {
    "id": 1197231713,
    "agency_id": "labor-department",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=V"
  },
  {
    "id": 11448081,
    "agency_id": "benefits-review-board",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=VII"
  },
  {
    "id": 1355778151,
    "agency_id": "employee-benefits-security-administration",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XXV"
  },
  {
    "id": 18226401,
    "agency_id": "employees-compensation-appeals-board",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=IV"
  },
  {
    "id": 2059284678,
    "agency_id": "employment-and-training-administration",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=V"
  },
  {
    "id": 1249647776,
    "agency_id": "mine-safety-and-health-administration",
    "title": 30,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=30/chapter=I"
  },
  {
    "id": 968802092,
    "agency_id": "occupational-safety-and-health-administration",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XVII"
  },
  {
    "id": 163324803,
    "agency_id": "office-of-assistant-secretary-for-veterans'-employment-and-training-service",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=IX"
  },
  {
    "id": 907192190,
    "agency_id": "office-of-assistant-secretary-for-veterans'-employment-and-training-service",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=61"
  },
  {
    "id": 1688447667,
    "agency_id": "federal-contract-compliance-programs-office",
    "title": 41,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=41/chapter=60"
  },
  {
    "id": 240136928,
    "agency_id": "labor-management-standards-office",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=II"
  },
  {
    "id": 1039198128,
    "agency_id": "labor-management-standards-office",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=IV"
  },
  {
    "id": 108096511,
    "agency_id": "office-of-secretary-of-labor",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=A"
  },
  {
    "id": 1683952131,
    "agency_id": "workers-compensation-programs-office",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=I"
  },
  {
    "id": 1211635838,
    "agency_id": "workers-compensation-programs-office",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=VI"
  },
  {
    "id": 44158227,
    "agency_id": "wage-and-hour-division",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=V"
  },
  {
    "id": 1991108649,
    "agency_id": "legal-services-corporation",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XVI"
  },
  {
    "id": 117070785,
    "agency_id": "national-commission-on-libraries-and-information-science",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XVII"
  },
  {
    "id": 223755600,
    "agency_id": "library-of-congress",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=VII"
  },
  {
    "id": 960471533,
    "agency_id": "library-of-congress",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=III"
  },
  {
    "id": 2013846792,
    "agency_id": "library-of-congress",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=II"
  },
  {
    "id": 1766414173,
    "agency_id": "copyright-royalty-board",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=III"
  },
  {
    "id": 2090750278,
    "agency_id": "copyright-office-library-of-congress",
    "title": 37,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=37/chapter=II"
  },
  {
    "id": 1539938261,
    "agency_id": "management-and-budget-office",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=A"
  },
  {
    "id": 1880269183,
    "agency_id": "management-and-budget-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=III"
  },
  {
    "id": 2139323751,
    "agency_id": "management-and-budget-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXVII"
  },
  {
    "id": 1850357472,
    "agency_id": "management-and-budget-office",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=99"
  },
  {
    "id": 1850357472,
    "agency_id": "management-and-budget-office",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=99"
  },
  {
    "id": 1500090515,
    "agency_id": "federal-procurement-policy-office",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=99"
  },
  {
    "id": 1534560956,
    "agency_id": "marine-mammal-commission",
    "title": 50,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=50/chapter=V"
  },
  {
    "id": 1178106746,
    "agency_id": "merit-systems-protection-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=II"
  },
  {
    "id": 2136528989,
    "agency_id": "merit-systems-protection-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXIV"
  },
  {
    "id": 1588801680,
    "agency_id": "office-for-micronesian-status-negotiations",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XXVII"
  },
  {
    "id": 492013688,
    "agency_id": "military-compensation-and-retirement-modernization-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XCIX"
  },
  {
    "id": 848369474,
    "agency_id": "national-commission-on-military-national-and-public-service",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=IV"
  },
  {
    "id": 801561256,
    "agency_id": "millennium-challenge-corporation",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=XIII"
  },
  {
    "id": 1524703059,
    "agency_id": "morris-k-udall-and-stewart-l-udall-foundation",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=XVI"
  },
  {
    "id": 1618623639,
    "agency_id": "national-aeronautics-and-space-administration",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XVIII"
  },
  {
    "id": 1384958791,
    "agency_id": "national-aeronautics-and-space-administration",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LIX"
  },
  {
    "id": 1073181732,
    "agency_id": "national-aeronautics-and-space-administration",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=V"
  },
  {
    "id": 550568043,
    "agency_id": "national-aeronautics-and-space-administration",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=18"
  },
  {
    "id": 1308762988,
    "agency_id": "corporation-for-national-and-community-service",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXII"
  },
  {
    "id": 1851041030,
    "agency_id": "corporation-for-national-and-community-service",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XII"
  },
  {
    "id": 356935789,
    "agency_id": "corporation-for-national-and-community-service",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XXV"
  },
  {
    "id": 354654471,
    "agency_id": "national-archives-and-records-administration",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXVI"
  },
  {
    "id": 2027347988,
    "agency_id": "national-archives-and-records-administration",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXVI"
  },
  {
    "id": 143951670,
    "agency_id": "national-archives-and-records-administration",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=XII"
  },
  {
    "id": 805588090,
    "agency_id": "national-archives-and-records-administration",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XX"
  },
  {
    "id": 1417486508,
    "agency_id": "national-archives-and-records-administration",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=II"
  },
  {
    "id": 418393055,
    "agency_id": "information-security-oversight-office",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XX"
  },
  {
    "id": 212163740,
    "agency_id": "federal-register-office",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=II"
  },
  {
    "id": 1401104962,
    "agency_id": "national-capital-planning-commission",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=IV"
  },
  {
    "id": 369174827,
    "agency_id": "national-capital-planning-commission",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=VI"
  },
  {
    "id": 1999669577,
    "agency_id": "national-counterintelligence-center",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XVIII"
  },
  {
    "id": 1790855273,
    "agency_id": "national-credit-union-administration",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXXXVI"
  },
  {
    "id": 962197429,
    "agency_id": "national-credit-union-administration",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=VII"
  },
  {
    "id": 1885547902,
    "agency_id": "national-crime-prevention-and-privacy-compact-council",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=IX"
  },
  {
    "id": 415316024,
    "agency_id": "office-of-national-drug-control-policy",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXVI"
  },
  {
    "id": 1227507759,
    "agency_id": "office-of-national-drug-control-policy",
    "title": 21,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=21/chapter=III"
  },
  {
    "id": 1614462157,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=XI"
  },
  {
    "id": 586289217,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXI"
  },
  {
    "id": 512834949,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXVII"
  },
  {
    "id": 1423058360,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXII"
  },
  {
    "id": 1187364541,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LV"
  },
  {
    "id": 431302676,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXIII"
  },
  {
    "id": 1626861541,
    "agency_id": "national-foundation-on-the-arts-and-the-humanities",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LVI"
  },
  {
    "id": 1049828640,
    "agency_id": "institute-of-museum-and-library-services",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXI"
  },
  {
    "id": 1651111123,
    "agency_id": "institute-of-museum-and-library-services",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXVII"
  },
  {
    "id": 1742662641,
    "agency_id": "national-endowment-for-the-arts",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXII"
  },
  {
    "id": 1234707592,
    "agency_id": "national-endowment-for-the-arts",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LV"
  },
  {
    "id": 701763573,
    "agency_id": "national-endowment-for-the-humanities",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXIII"
  },
  {
    "id": 1894869305,
    "agency_id": "national-endowment-for-the-humanities",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LVI"
  },
  {
    "id": 1328300559,
    "agency_id": "national-labor-relations-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXI"
  },
  {
    "id": 1114324413,
    "agency_id": "national-labor-relations-board",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=I"
  },
  {
    "id": 1941931535,
    "agency_id": "national-mediation-board",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=CI"
  },
  {
    "id": 613205761,
    "agency_id": "national-mediation-board",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=X"
  },
  {
    "id": 1214365739,
    "agency_id": "national-railroad-adjustment-board",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=III"
  },
  {
    "id": 591587700,
    "agency_id": "national-railroad-passenger-corporation",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=VII"
  },
  {
    "id": 1205035241,
    "agency_id": "national-science-foundation",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXV"
  },
  {
    "id": 299602805,
    "agency_id": "national-science-foundation",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLIII"
  },
  {
    "id": 2027798327,
    "agency_id": "national-science-foundation",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=VI"
  },
  {
    "id": 1796988824,
    "agency_id": "national-science-foundation",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=25"
  },
  {
    "id": 88625107,
    "agency_id": "national-transportation-safety-board",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=VIII"
  },
  {
    "id": 1619143877,
    "agency_id": "navajo-and-hopi-indian-relocation-office",
    "title": 25,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=25/chapter=IV"
  },
  {
    "id": 1609608359,
    "agency_id": "neighborhood-reinvestment-corporation",
    "title": 24,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=24/chapter=XXV"
  },
  {
    "id": 855976420,
    "agency_id": "northeast-interstate-low-level-radioactive-waste-commission",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=XVIII"
  },
  {
    "id": 2046477058,
    "agency_id": "nuclear-regulatory-commission",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XX"
  },
  {
    "id": 1994163077,
    "agency_id": "nuclear-regulatory-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLVIII"
  },
  {
    "id": 1623188974,
    "agency_id": "nuclear-regulatory-commission",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=I"
  },
  {
    "id": 668548352,
    "agency_id": "nuclear-regulatory-commission",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=20"
  },
  {
    "id": 1463369112,
    "agency_id": "nuclear-waste-technical-review-board",
    "title": 10,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=10/chapter=XIII"
  },
  {
    "id": 189461771,
    "agency_id": "occupational-safety-and-health-review-commission",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XX"
  },
  {
    "id": 326080331,
    "agency_id": "oklahoma-city-national-memorial-trust",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=XV"
  },
  {
    "id": 162063414,
    "agency_id": "peace-corps",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXXVII"
  },
  {
    "id": 210568301,
    "agency_id": "peace-corps",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=III"
  },
  {
    "id": 1528114507,
    "agency_id": "pennsylvania-avenue-development-corporation",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=IX"
  },
  {
    "id": 264450510,
    "agency_id": "pension-benefit-guaranty-corporation",
    "title": 29,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=29/chapter=XL"
  },
  {
    "id": 1424084677,
    "agency_id": "personnel-management-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=I"
  },
  {
    "id": 1097376719,
    "agency_id": "personnel-management-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=IV"
  },
  {
    "id": 231392912,
    "agency_id": "personnel-management-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXXV"
  },
  {
    "id": 1118102773,
    "agency_id": "personnel-management-office",
    "title": 45,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=45/chapter=VIII"
  },
  {
    "id": 66516312,
    "agency_id": "personnel-management-office",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=16"
  },
  {
    "id": 911802990,
    "agency_id": "personnel-management-office",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=17"
  },
  {
    "id": 1877153938,
    "agency_id": "personnel-management-office",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=21"
  },
  {
    "id": 138674305,
    "agency_id": "postal-regulatory-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XLVI"
  },
  {
    "id": 2084458134,
    "agency_id": "postal-regulatory-commission",
    "title": 39,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=39/chapter=III"
  },
  {
    "id": 197654505,
    "agency_id": "postal-service",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LX"
  },
  {
    "id": 1020245063,
    "agency_id": "postal-service",
    "title": 39,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=39/chapter=I"
  },
  {
    "id": 852884685,
    "agency_id": "presidio-trust",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=X"
  },
  {
    "id": 630333616,
    "agency_id": "privacy-and-civil-liberties-oversight-board",
    "title": 6,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=6/chapter=X"
  },
  {
    "id": 675523866,
    "agency_id": "railroad-retirement-board",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=II"
  },
  {
    "id": 391080959,
    "agency_id": "securities-and-exchange-commission",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXXIV"
  },
  {
    "id": 845800962,
    "agency_id": "securities-and-exchange-commission",
    "title": 17,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=17/chapter=II"
  },
  {
    "id": 605571130,
    "agency_id": "selective-service-system",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XVI"
  },
  {
    "id": 1517948529,
    "agency_id": "small-business-administration",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXVII"
  },
  {
    "id": 1394699965,
    "agency_id": "small-business-administration",
    "title": 13,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=13/chapter=I"
  },
  {
    "id": 2078581273,
    "agency_id": "smithsonian-institution",
    "title": 36,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=36/chapter=V"
  },
  {
    "id": 1169757207,
    "agency_id": "social-security-administration",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XXIII"
  },
  {
    "id": 301312193,
    "agency_id": "social-security-administration",
    "title": 20,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=20/chapter=III"
  },
  {
    "id": 797100887,
    "agency_id": "social-security-administration",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=23"
  },
  {
    "id": 1979563399,
    "agency_id": "special-counsel-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=VIII"
  },
  {
    "id": 17949663,
    "agency_id": "special-counsel-office",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=CII"
  },
  {
    "id": 369539272,
    "agency_id": "state-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=VI"
  },
  {
    "id": 710908627,
    "agency_id": "state-department",
    "title": 22,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=22/chapter=I"
  },
  {
    "id": 1322060781,
    "agency_id": "state-department",
    "title": 28,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=28/chapter=XI"
  },
  {
    "id": 1412272890,
    "agency_id": "state-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=6"
  },
  {
    "id": 744052549,
    "agency_id": "surface-transportation-board",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=X"
  },
  {
    "id": 803397526,
    "agency_id": "susquehanna-river-basin-commission",
    "title": 18,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=18/chapter=VIII"
  },
  {
    "id": 1535748707,
    "agency_id": "tennessee-valley-authority",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=LXIX"
  },
  {
    "id": 1859413135,
    "agency_id": "tennessee-valley-authority",
    "title": 18,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=18/chapter=XIII"
  },
  {
    "id": 2142719126,
    "agency_id": "transportation-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=XII"
  },
  {
    "id": 158191575,
    "agency_id": "transportation-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=L"
  },
  {
    "id": 228446583,
    "agency_id": "transportation-department",
    "title": 44,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=44/chapter=IV"
  },
  {
    "id": 1274515896,
    "agency_id": "transportation-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=12"
  },
  {
    "id": 1338208859,
    "agency_id": "transportation-department",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=I"
  },
  {
    "id": 1858396596,
    "agency_id": "transportation-department",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=III"
  },
  {
    "id": 2114246211,
    "agency_id": "transportation-department",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=I"
  },
  {
    "id": 676202620,
    "agency_id": "transportation-department",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=II"
  },
  {
    "id": 654500651,
    "agency_id": "transportation-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=III"
  },
  {
    "id": 490382152,
    "agency_id": "transportation-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=II"
  },
  {
    "id": 120057933,
    "agency_id": "transportation-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=VI"
  },
  {
    "id": 1583146965,
    "agency_id": "transportation-department",
    "title": 33,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=33/chapter=IV"
  },
  {
    "id": 807141971,
    "agency_id": "transportation-department",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=II"
  },
  {
    "id": 676202620,
    "agency_id": "transportation-department",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=II"
  },
  {
    "id": 1991293694,
    "agency_id": "transportation-department",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=III"
  },
  {
    "id": 824641994,
    "agency_id": "transportation-department",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=IV"
  },
  {
    "id": 2086047056,
    "agency_id": "transportation-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=V"
  },
  {
    "id": 1427052413,
    "agency_id": "transportation-department",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=II"
  },
  {
    "id": 896339812,
    "agency_id": "transportation-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=A"
  },
  {
    "id": 881490621,
    "agency_id": "transportation-department",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=I"
  },
  {
    "id": 2053702659,
    "agency_id": "federal-aviation-administration",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=I"
  },
  {
    "id": 1557155236,
    "agency_id": "commercial-space-transportation-office",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=III"
  },
  {
    "id": 1422522426,
    "agency_id": "federal-highway-administration",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=I"
  },
  {
    "id": 2012154735,
    "agency_id": "federal-highway-administration",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=II"
  },
  {
    "id": 2033752673,
    "agency_id": "federal-motor-carrier-safety-administration",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=III"
  },
  {
    "id": 96661206,
    "agency_id": "federal-railroad-administration",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=II"
  },
  {
    "id": 1613262368,
    "agency_id": "federal-transit-administration",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=VI"
  },
  {
    "id": 1544469252,
    "agency_id": "great-lakes-st-lawrence-seaway-development-corporation",
    "title": 33,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=33/chapter=IV"
  },
  {
    "id": 2013291521,
    "agency_id": "maritime-administration",
    "title": 46,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=46/chapter=II"
  },
  {
    "id": 1877727667,
    "agency_id": "national-highway-traffic-safety-administration",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=II"
  },
  {
    "id": 2031800781,
    "agency_id": "national-highway-traffic-safety-administration",
    "title": 23,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=23/chapter=III"
  },
  {
    "id": 417822100,
    "agency_id": "national-highway-traffic-safety-administration",
    "title": 47,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=47/chapter=IV"
  },
  {
    "id": 625880463,
    "agency_id": "national-highway-traffic-safety-administration",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=V"
  },
  {
    "id": 1151828246,
    "agency_id": "office-of-secretary-(aviation-proceedings)",
    "title": 14,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=14/chapter=II"
  },
  {
    "id": 1225837198,
    "agency_id": "office-of-secretary-of-transportation",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=A"
  },
  {
    "id": 1899245790,
    "agency_id": "pipeline-and-hazardous-materials-safety-administration",
    "title": 49,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=49/chapter=I"
  },
  {
    "id": 1528281384,
    "agency_id": "treasury-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=X"
  },
  {
    "id": 494757490,
    "agency_id": "treasury-department",
    "title": 5,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=5/chapter=XXI"
  },
  {
    "id": 145146214,
    "agency_id": "treasury-department",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XV"
  },
  {
    "id": 802651099,
    "agency_id": "treasury-department",
    "title": 17,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=17/chapter=IV"
  },
  {
    "id": 1936466171,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=IX"
  },
  {
    "id": 1300271874,
    "agency_id": "treasury-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=10"
  },
  {
    "id": 913527230,
    "agency_id": "treasury-department",
    "title": 27,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=27/chapter=I"
  },
  {
    "id": 103430154,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=VI"
  },
  {
    "id": 861422828,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=II"
  },
  {
    "id": 995173179,
    "agency_id": "treasury-department",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XVIII"
  },
  {
    "id": 759921508,
    "agency_id": "treasury-department",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=I"
  },
  {
    "id": 1047336756,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=X"
  },
  {
    "id": 861422828,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=II"
  },
  {
    "id": 642535995,
    "agency_id": "treasury-department",
    "title": 26,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=26/chapter=I"
  },
  {
    "id": 1581958433,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=I"
  },
  {
    "id": 1332867301,
    "agency_id": "treasury-department",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XVI"
  },
  {
    "id": 2066544921,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=V"
  },
  {
    "id": 997081967,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=VIII"
  },
  {
    "id": 1571097063,
    "agency_id": "treasury-department",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=A"
  },
  {
    "id": 675547035,
    "agency_id": "alcohol-and-tobacco-tax-and-trade-bureau",
    "title": 27,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=27/chapter=I"
  },
  {
    "id": 1719960990,
    "agency_id": "engraving-and-printing-bureau",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=VI"
  },
  {
    "id": 1487362446,
    "agency_id": "bureau-of-the-fiscal-service",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=II"
  },
  {
    "id": 1346443090,
    "agency_id": "community-development-financial-institutions-fund",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XVIII"
  },
  {
    "id": 1972656366,
    "agency_id": "comptroller-of-the-currency",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=I"
  },
  {
    "id": 792440871,
    "agency_id": "financial-crimes-enforcement-network",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=X"
  },
  {
    "id": 1180125892,
    "agency_id": "fiscal-service",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=II"
  },
  {
    "id": 1692228160,
    "agency_id": "internal-revenue-service",
    "title": 26,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=26/chapter=I"
  },
  {
    "id": 205260409,
    "agency_id": "monetary-offices",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=I"
  },
  {
    "id": 967833488,
    "agency_id": "office-of-financial-research",
    "title": 12,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=12/chapter=XVI"
  },
  {
    "id": 498723012,
    "agency_id": "foreign-assets-control-office",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=V"
  },
  {
    "id": 16128257,
    "agency_id": "investment-security-office",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=VIII"
  },
  {
    "id": 888808214,
    "agency_id": "office-of-secretary-of-the-treasury",
    "title": 31,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=31/chapter=A"
  },
  {
    "id": 1561433127,
    "agency_id": "trade-representative-office-of-united-states",
    "title": 15,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=15/chapter=XX"
  },
  {
    "id": 2071993253,
    "agency_id": "utah-reclamation-mitigation-and-conservation-commission",
    "title": 43,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=43/chapter=III"
  },
  {
    "id": 2015801367,
    "agency_id": "veterans-affairs-department",
    "title": 2,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=2/chapter=VIII"
  },
  {
    "id": 2076780288,
    "agency_id": "veterans-affairs-department",
    "title": 38,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=38/chapter=I"
  },
  {
    "id": 1749092152,
    "agency_id": "veterans-affairs-department",
    "title": 48,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=48/chapter=8"
  },
  {
    "id": 578750457,
    "agency_id": "office-of-vice-president-of-the-united-states",
    "title": 32,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=32/chapter=XXVIII"
  },
  {
    "id": 1718625493,
    "agency_id": "water-resources-council",
    "title": 18,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=18/chapter=VI"
  },
  {
    "id": 1361334491,
    "agency_id": "president's-commission-on-white-house-fellowships",
    "title": 1,
    "subheading": null,
    "is_primary": true,
    "ordinal": null,
    "node_id": "us/federal/ecfr/title=1/chapter=IV"
  }
]$JSON$::jsonb) ON CONFLICT (agency_id, node_id) DO NOTHING;
