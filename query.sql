-- create database
CREATE DATABASE flask_blogs;

-- create table users
 CREATE TABLE users (
       id serial PRIMARY KEY,
       username  VARCHAR ( 200 ) NOT NULL,
       password VARCHAR ( 150 ) NOT NULL 
       );   

 -- create table blogs

 CREATE TABLE blogs (
       id serial PRIMARY KEY,
       title VARCHAR ( 200 ) NOT NULL,
       content TEXT NOT NULL,  
       created_on TIMESTAMP, 
       creator VARCHAR ( 150 ) NOT NULL 
       );           

       