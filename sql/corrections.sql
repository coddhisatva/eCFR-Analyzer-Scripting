CREATE TABLE corrections (
    id SERIAL PRIMARY KEY,
    node_id TEXT REFERENCES nodes(id) ON DELETE CASCADE,
    title INTEGER NOT NULL,
    corrective_action TEXT,
    error_corrected DATE,
    error_occurred DATE,
	correction_duration INTEGER,
    fr_citation TEXT,
    position INTEGER,
    year INTEGER,
    metadata JSONB
);

-- Index for finding corrections by node
CREATE INDEX corrections_node_idx ON corrections(node_id);

-- Index for finding corrections by date ranges
CREATE INDEX corrections_corrected_idx ON corrections(error_corrected);
CREATE INDEX corrections_occurred_idx ON corrections(error_occurred);

-- Index for finding corrections by title
CREATE INDEX corrections_title_idx ON corrections(title);

--longest correction duration
CREATE INDEX corrections_duration_idx ON corrections(correction_duration);



