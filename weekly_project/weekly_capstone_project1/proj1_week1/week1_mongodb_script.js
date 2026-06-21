// ============================================================
// RETAIL SALES PERFORMANCE DASHBOARD - WEEK 1
// MongoDB Script: Campaign Feedback Storage + Indexing
// ============================================================

db = db.getSiblingDB('retail_campaigns_db');

// ============================================================
// Create collection: campaign_feedback
// ============================================================

db.createCollection("campaign_feedback");

// ============================================================
// Insert promotional campaign feedback documents
// ============================================================

db.campaign_feedback.insertMany([
  {
    campaign_id: "CMP001",
    campaign_name: "Summer Electronics Sale",
    store_id: 1,
    region: "South",
    product_category: "Electronics",
    feedback_text: "Great discounts, customers loved the deals on speakers.",
    rating: 4.5,
    feedback_date: new Date("2026-06-01"),
    customer_sentiment: "Positive"
  },
  {
    campaign_id: "CMP001",
    campaign_name: "Summer Electronics Sale",
    store_id: 2,
    region: "South",
    product_category: "Electronics",
    feedback_text: "Footfall increased but stock ran out quickly.",
    rating: 3.8,
    feedback_date: new Date("2026-06-02"),
    customer_sentiment: "Mixed"
  },
  {
    campaign_id: "CMP002",
    campaign_name: "Monsoon Apparel Fest",
    store_id: 3,
    region: "North",
    product_category: "Apparel",
    feedback_text: "Customers found pricing still high despite discount.",
    rating: 2.9,
    feedback_date: new Date("2026-06-03"),
    customer_sentiment: "Negative"
  },
  {
    campaign_id: "CMP003",
    campaign_name: "Fitness Week Promo",
    store_id: 4,
    region: "West",
    product_category: "Fitness",
    feedback_text: "Yoga mats and accessories sold extremely well.",
    rating: 4.8,
    feedback_date: new Date("2026-06-04"),
    customer_sentiment: "Positive"
  },
  {
    campaign_id: "CMP003",
    campaign_name: "Fitness Week Promo",
    store_id: 5,
    region: "East",
    product_category: "Fitness",
    feedback_text: "Limited awareness, foot traffic was lower than expected.",
    rating: 3.0,
    feedback_date: new Date("2026-06-05"),
    customer_sentiment: "Mixed"
  },
  {
    campaign_id: "CMP004",
    campaign_name: "Home Essentials Bonanza",
    store_id: 1,
    region: "South",
    product_category: "Home",
    feedback_text: "Desk lamps were a hit, customers asked for more variety.",
    rating: 4.2,
    feedback_date: new Date("2026-06-06"),
    customer_sentiment: "Positive"
  }
]);

// ============================================================
// Indexes: search by product_category and region
// ============================================================

db.campaign_feedback.createIndex({ product_category: 1 });
db.campaign_feedback.createIndex({ region: 1 });

// Compound index for combined searches
db.campaign_feedback.createIndex({ region: 1, product_category: 1 });

// ============================================================
// Sample Queries
// ============================================================

// Find all feedback for Electronics category
db.campaign_feedback.find({ product_category: "Electronics" });

// Find all feedback from South region
db.campaign_feedback.find({ region: "South" });

// Find feedback by region AND category (uses compound index)
db.campaign_feedback.find({ region: "South", product_category: "Electronics" });

// Average rating per campaign
db.campaign_feedback.aggregate([
  {
    $group: {
      _id: "$campaign_id",
      campaign_name: { $first: "$campaign_name" },
      avg_rating: { $avg: "$rating" },
      feedback_count: { $sum: 1 }
    }
  },
  { $sort: { avg_rating: -1 } }
]);

// Verify indexes were created
db.campaign_feedback.getIndexes();