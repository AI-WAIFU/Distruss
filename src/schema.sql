CREATE SCHEMA distruss_core;

DROP TABLE IF EXISTS federated_instances;
DROP TABLE IF EXISTS communities;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS post_votes;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS comment_votes;
DROP TABLE IF EXISTS gates;
DROP TABLE IF EXISTS user_gates;
DROP TABLE IF EXISTS community_gates;
DROP TABLE IF EXISTS community_bans;
DROP TABLE IF EXISTS sitewide_bans;

CREATE TABLE federated_instances (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  registration_time TIMESTAMP
  domain VARCHAR(512)
  public_key VARCHAR(10000)
);

CREATE TABLE communities (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP
  name VARCHAR(48)
  PRIMARY KEY(id)
);

CREATE TABLE users (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP
  salt BIT(256),
  username VARCHAR(48)
  password BIT(184)
  public_key varchar(10000)
  private_key varchar(10000)
  PRIMARY KEY(id)
  CONSTRAINT fk_domain
    FOREIGN KEY(domain)
      REFERENCES(domain.id)
);

CREATE TABLE posts (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP,
  error_code SMALLINT
  text VARCHAR(100000),
  url VARCHAR(32768),
  author BIGINT,
  community BIGINT,
  PRIMARY KEY(id),
  CONSTRAINT fk_author
    FOREIGN KEY(author)
      REFERENCES(users.id),
  CONSTRAINT fk_community
    FOREIGN KEY(community)
      REFERENCES(community.id)
);

CREATE TABLE post_votes (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP,
  post BIGINT,
  user BIGINT,
  PRIMARY KEY(id),
  CONSTRAINT fk_user
    FOREIGN KEY(user)
      REFERENCES(users.id),
  CONSTRAINT fk_post
    FOREIGN KEY(post)
      REFERENCES(posts.id)
);

CREATE TABLE comments (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP
  error_code SMALLINT
  text VARCHAR(100000),
  parent BIGINT,
  author BIGINT,
  post BIGINT,
  PRIMARY KEY(id),
  CONSTRAINT fk_parent
    FOREIGN KEY(parent)
      REFERENCES(comments.id),
  CONSTRAINT fk_post
    FOREIGN KEY(post)
      REFERENCES(posts.id),
  CONSTRAINT fk_author
    FOREIGN KEY(author)
      REFERENCES(users.id)
);


CREATE TABLE comment_votes (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP
  comment BIGINT,
  user BIGINT,
  PRIMARY KEY(id),
  CONSTRAINT fk_user
    FOREIGN KEY(user)
      REFERENCES(users.id),
  CONSTRAINT fk_comment
    FOREIGN KEY(comment)
      REFERENCES(comments.id)
);


CREATE TABLE gates (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP,
  name VARCHAR(128),
  descripton VARCHAR(100000),
  url VARCHAR(32768),
);

CREATE TABLE user_gates (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP,
  expiration_time TIMESTAMP,
  gate BIGINT,
  user_uuid UUID,
  user_domain VARCHAR(512)
  CONSTRAINT fk_gate
    FOREIGN KEY(gate)
      REFERENCES(gates.id)
)

CREATE TABLE community_gates (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP,
  community BIGINT
  gate_uuid UUID,
  gate_domain VARCHAR(512),
  permission_level SMALLINT,
  CONSTRAINT fk_community
    FOREIGN KEY(community)
      REFERENCES(communities.id)
);


CREATE TABLE bans (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY,
  uuid UUID UNIQUE,
  creation_time TIMESTAMP,
  expiration_time TIMESTAMP,
  user_UUID uuid,
  user_domain VARCHAR(512),
  reason VARCHAR(100000),
  community BIGINT
);

























