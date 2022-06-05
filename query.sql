-- create database
CREATE DATABASE flask_blogs;

-- create table users
 CREATE TABLE users (
       id serial PRIMARY KEY,
       username  VARCHAR ( 200 ) NOT NULL,
       password VARCHAR ( 150 ) NOT NULL 
       );

-- insert one admin user so that can login first time & add blogs: 
INSERT INTO users(username, password) values('username@username.com', 'password')          
-- when logging in first time, use this or create your own in database.

 -- create table blogs

 CREATE TABLE blogs (
       id serial PRIMARY KEY,
       title VARCHAR ( 200 ) NOT NULL,
       content TEXT NOT NULL, 
       img_url VARCHAR ( 200 ) NOT NULL, 
       created_on TIMESTAMP, 
       creator VARCHAR ( 150 ) NOT NULL 
       );           

       