CREATE TABLE agencies (
    id TEXT PRIMARY KEY,  -- Using slug as ID for readability
    name TEXT NOT NULL,
    short_name TEXT,
    display_name TEXT,
    sortable_name TEXT,
    parent_id TEXT REFERENCES agencies(id),  -- Hierarchical structure
    depth INTEGER DEFAULT 0,  -- Hierarchy depth (0 for top-level agencies)
    agency_type TEXT,  -- 'beg', 'middle', 'zed'
    metadata JSONB  -- For flexible storage of additional data
);

-- Indexes for agency hierarchy navigation --
-- For list subagenciesi in agency view
CREATE INDEX agencies_parent_idx ON agencies(parent_id);

-- for agencies page
CREATE INDEX agencies_beg_type_idx ON agencies(agency_type) WHERE agency_type = 'beg';


CREATE TABLE cfr_references (
    id SERIAL PRIMARY KEY,
    agency_id TEXT NOT NULL REFERENCES agencies(id) ON DELETE SET NULL,
    title INTEGER NOT NULL,
    subheading TEXT,
    is_primary BOOLEAN DEFAULT true,
    ordinal INTEGER,
    node_id TEXT REFERENCES nodes(id),  -- Direct link to the nodes table
    UNIQUE(agency_id, node_id)
);

CREATE INDEX cfr_references_agency_idx ON cfr_references(agency_id);



--hard part ******** start--
CREATE TABLE agency_node_mappings (
    id SERIAL PRIMARY KEY,
    agency_id TEXT NOT NULL REFERENCES agencies(id),
    node_id TEXT NOT NULL REFERENCES nodes(id),
    is_primary BOOLEAN DEFAULT false,  -- Is this the primary agency for this node
    is_direct_reference BOOLEAN DEFAULT false,  -- Is this a direct CFR reference vs. inherited
    relationship_type TEXT,  -- Type of relationship (regulatory, advisory, etc.)
    metadata JSONB,  -- Additional information about the relationship
    UNIQUE(agency_id, node_id)  -- Prevent duplicate mappings
);





-- query, filter by agency (More, like sql in agency node strat)
CREATE INDEX agency_node_mappings_agency_idx ON agency_node_mappings(agency_id);
-- see agencies under node page
CREATE INDEX agency_node_mappings_node_idx ON agency_node_mappings(node_id);
--hard part end ************---

-- Index for efficient querying on these metrics
CREATE INDEX agencies_word_count_idx ON agencies(((metadata->'precomputed_metrics'->>'word_count')::int))
WHERE metadata->'precomputed_metrics'->>'word_count' IS NOT NULL;

CREATE INDEX agencies_child_count_idx ON agencies(((metadata->'precomputed_metrics'->>'child_count')::int))
WHERE metadata->'precomputed_metrics'->>'child_count' IS NOT NULL;;




