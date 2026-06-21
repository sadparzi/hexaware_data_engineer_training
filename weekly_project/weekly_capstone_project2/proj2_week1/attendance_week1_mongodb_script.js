// ============================================================
// EMPLOYEE ATTENDANCE & PRODUCTIVITY TRACKER - WEEK 1
// MongoDB Script: Task Feedback & Notes + Indexing
// ============================================================

db = db.getSiblingDB('attendance_tracker_db');

// ============================================================
// Create collection: task_feedback
// ============================================================

db.createCollection("task_feedback");

// ============================================================
// Insert unstructured task feedback / notes
// ============================================================

db.task_feedback.insertMany([
  {
    employee_id: 1,
    employee_name: "Rahul Sharma",
    department: "Engineering",
    feedback_date: new Date("2026-06-01"),
    note: "Completed sprint tasks ahead of schedule, good code quality.",
    manager_comment: "Keep up the pace, consider mentoring juniors.",
    sentiment: "Positive"
  },
  {
    employee_id: 2,
    employee_name: "Priya Reddy",
    department: "Engineering",
    feedback_date: new Date("2026-06-01"),
    note: "Resolved all assigned bugs, also helped debug a teammate's issue.",
    manager_comment: "Excellent collaboration this week.",
    sentiment: "Positive"
  },
  {
    employee_id: 3,
    employee_name: "Amit Kumar",
    department: "Sales",
    feedback_date: new Date("2026-06-01"),
    note: "Missed two client follow-ups, came in late.",
    manager_comment: "Needs improvement in time management.",
    sentiment: "Negative"
  },
  {
    employee_id: 5,
    employee_name: "Farhan Ali",
    department: "Sales",
    feedback_date: new Date("2026-06-01"),
    note: "Absent without prior notice, team had to cover his client calls.",
    manager_comment: "Follow up required regarding attendance pattern.",
    sentiment: "Negative"
  },
  {
    employee_id: 6,
    employee_name: "Neha Singh",
    department: "Marketing",
    feedback_date: new Date("2026-06-02"),
    note: "Delivered campaign assets on time, good creative input.",
    manager_comment: "Solid performance, on track for the quarter.",
    sentiment: "Positive"
  },
  {
    employee_id: 3,
    employee_name: "Amit Kumar",
    department: "Sales",
    feedback_date: new Date("2026-06-02"),
    note: "No task updates submitted, unclear on current workload status.",
    manager_comment: "Schedule a 1:1 to check in.",
    sentiment: "Negative"
  },
  {
    employee_id: 8,
    employee_name: "Meera Nair",
    department: "Marketing",
    feedback_date: new Date("2026-06-02"),
    note: "Behind on content calendar, but flagged the blocker early.",
    manager_comment: "Appreciate the proactive communication.",
    sentiment: "Mixed"
  }
]);

// ============================================================
// Indexes: fast querying by employee_id and department
// ============================================================

db.task_feedback.createIndex({ employee_id: 1 });
db.task_feedback.createIndex({ department: 1 });

// Compound index for combined lookups
db.task_feedback.createIndex({ department: 1, employee_id: 1 });

// ============================================================
// Sample Queries
// ============================================================

// All feedback for a specific employee
db.task_feedback.find({ employee_id: 3 });

// All feedback for a department
db.task_feedback.find({ department: "Sales" });

// All negative sentiment notes (potential issues to flag for HR)
db.task_feedback.find({ sentiment: "Negative" });

// Count feedback entries by sentiment per department
db.task_feedback.aggregate([
  {
    $group: {
      _id: { department: "$department", sentiment: "$sentiment" },
      count: { $sum: 1 }
    }
  },
  { $sort: { "_id.department": 1 } }
]);

// Verify indexes
db.task_feedback.getIndexes();
