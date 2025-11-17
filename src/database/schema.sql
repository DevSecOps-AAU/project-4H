CREATE TABLE "users" (
  "id" uuid PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "password" text,
  "created_at" timestamp DEFAULT 'now()',
  "last_login" timestamp DEFAULT 'now()'
);

CREATE TABLE "History" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "input_text" text,
  "sentiment_label" text,
  "confident_score" text,
  "analysis_timestamp" timestamp DEFAULT 'now()'
);

CREATE TABLE "Performance" (
  "id" uuid,
  "model_version" int,
  "accuracy" int,
  "f1_score" int,
  "traning_date" timestamp DEFAULT 'now()',
  "is_active" bool,
  PRIMARY KEY ("id", "model_version")
);

ALTER TABLE "History" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");