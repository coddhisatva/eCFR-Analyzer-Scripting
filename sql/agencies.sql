DROP TABLE IF EXISTS agencies CASCADE;
DROP TABLE IF EXISTS cfr_references CASCADE;
DROP TABLE IF EXISTS agency_node_mappings CASCADE;

CREATE TABLE IF NOT EXISTS agencies (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    parent_id TEXT REFERENCES agencies(id),  -- Hierarchical structure
    depth INTEGER DEFAULT 0,  -- Hierarchy depth (0 for top-level agencies)
    num_children INTEGER DEFAULT 0,
    num_cfr INTEGER DEFAULT 0,
    num_words INTEGER DEFAULT 0,
    num_sections INTEGER DEFAULT 0,
    cfr_references TEXT[] DEFAULT '{}'
);

-- Index for agency lookups
CREATE INDEX IF NOT EXISTS agencies_id_idx ON agencies(id);

-- Index for agency name searches
CREATE INDEX IF NOT EXISTS agencies_name_idx ON agencies(name);

-- Index for agency metrics
CREATE INDEX IF NOT EXISTS agencies_metrics_idx ON agencies(num_children, num_cfr, num_words, num_sections);

-- Index for agency hierarchy navigation
CREATE INDEX IF NOT EXISTS agencies_parent_idx ON agencies(parent_id);

-- Index for depth-based queries
CREATE INDEX IF NOT EXISTS agencies_depth_idx ON agencies(depth);

CREATE TABLE cfr_references (
    id SERIAL PRIMARY KEY,
    agency_id TEXT NOT NULL REFERENCES agencies(id) ON DELETE SET NULL,
    title INTEGER NOT NULL,
    subheading TEXT,
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
    metadata JSONB,  -- Additional information about the relationship
    UNIQUE(agency_id, node_id)  -- Prevent duplicate mappings
);

-- query, filter by agency (More, like sql in agency node strat)
CREATE INDEX agency_node_mappings_agency_idx ON agency_node_mappings(agency_id);
-- see agencies under node page
CREATE INDEX agency_node_mappings_node_idx ON agency_node_mappings(node_id);
--hard part end ************---

-- order by numsections
CREATE INDEX agencies_num_sections_idx ON agencies(num_sections);

-- order by numwords
CREATE INDEX agencies_num_words_idx ON agencies(num_words);

-- order by numcorrections
CREATE INDEX agencies_num_corrections_idx ON agencies(num_corrections);


