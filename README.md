# Django IPL Project

## Objective
- Get familiar with Django MVC
- Get familiar with Django ORM - migrations, queries with joins and aggregations, using transactions

## Step 1
- Take only the IPL dataset. Not the other ones.
- Make sure you have set up tables correctly having foreign key relationships.
- Create a custom Django command and import the dataset into tables. Use atomic transactions.

**Questions:**
1. **What is the use of a transaction?**
   - A transaction ensures the consistency and integrity of the database by allowing a series of database operations to be treated as a single, atomic unit. Either all operations within the transaction are completed, or none of them are.

2. **Why atomic transactions?**
   - Atomic transactions ensure that database operations are performed in an all-or-nothing fashion. If any part of the transaction fails, the entire transaction is rolled back, maintaining the integrity of the data.

## Step 2

- Create four routes in a `views.py` that calculate results using Django ORM queries and return JSON:
  1. Number of matches played per year for all the years in IPL.
  2. Number of matches won per team per year in IPL.
  3. Extra runs conceded per team in the year 2016.
  4. Top 10 economical bowlers in the year 2015.

## Step 3
- Have another set of four routes for displaying the charts which hit the previous four routes and use HighCharts to render. You may have to figure out Django templates for this step.

---
