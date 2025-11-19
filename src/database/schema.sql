-- Users table
CREATE TABLE
  users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    last_login_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

-- Analysis history table
CREATE TABLE
  analysis_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    user_id UUID REFERENCES users (id) ON DELETE CASCADE,
    input_text TEXT,
    sentiment_label TEXT,
    confidence_score TEXT,
    last_analysis_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );

-- Model performance table
CREATE TABLE
  model_performance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
    model_version TEXT,
    accuracy TEXT,
    fl_score INTEGER,
    training_date TIMESTAMP NOT NULL DEFAULT NOW (),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW ()
  );