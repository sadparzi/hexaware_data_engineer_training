use edtech_capstone_db

db.createCollection("learners")
db.createCollection("instructors")
db.createCollection("courses")
db.createCollection("enrollments")

// inserting into collections 

db.learners.insertMany([
{
learner_id: 1,
name: "Rahul Sharma",
city: "Hyderabad",
experience_years: 2,
goal: "Data Engineer",
phone: "9876543210"
},
{
learner_id: 2,
name: "Priya Reddy",
city: "Bangalore",
experience_years: 4,
goal: "AI Engineer",
phone: "9876543211"
},
{
learner_id: 3,
name: "Amit Kumar",
city: "Mumbai",
experience_years: 1,
goal: "Data Analyst",
phone: null
},
{
learner_id: 4,
name: "Sneha Patel",
city: "Chennai",
experience_years: 6,
goal: "ML Engineer",
phone: "9876543213"
},
{
learner_id: 5,
name: "Farhan Ali",
city: "Delhi",
experience_years: 3,
goal: "Cloud Engineer",
phone: "9876543214"
},
{
learner_id: 6,
name: "Meera Nair",
city: "Pune",
experience_years: 0,
goal: "AI Engineer",
phone: null
}
])

db.instructors.insertMany([
{
instructor_id: 101,
instructor_name: "Abdullah Khan",
expertise: ["AI", "Data Engineering", "Cloud"],
rating: 4.9
},
{
instructor_id: 102,
instructor_name: "Neha Singh",
expertise: ["Power BI", "SQL", "Analytics"],
rating: 4.6
},
{
instructor_id: 103,
instructor_name: "Ravi Kumar",
expertise: ["Python", "Machine Learning"],
rating: 4.7
}
])

db.courses.insertMany([
{
course_id: 201,
course_name: "Data Engineering with Azure",
category: "Data Engineering",
instructor_id: 101,
price: 15000,
level: "Intermediate",
tools: ["SQL", "Python", "Azure Data Factory", "Databricks"]
},
{
course_id: 202,
course_name: "AI Engineer Roadmap",
category: "Artificial Intelligence",
instructor_id: 101,
price: 20000,
level: "Beginner",
tools: ["Python", "OpenAI", "Vector DB", "LangChain"]
},
{
course_id: 203,
course_name: "Power BI for Business",
category: "Analytics",
instructor_id: 102,
price: 8000,
level: "Beginner",
tools: ["Power BI", "Excel", "SQL"]
},
{
course_id: 204,
course_name: "Machine Learning Practical",
category: "Machine Learning",
instructor_id: 103,
price: 12000,
level: "Intermediate",
tools: ["Python", "Scikit-learn", "Pandas"]
},
{
course_id: 205,
course_name: "Cloud AI Engineer",
category: "Cloud",
instructor_id: 101,
price: 18000,
level: "Advanced",
tools: ["Azure", "AWS", "GCP", "AI Services"]
}
])

db.enrollments.insertMany([
{
enrollment_id: 1001,
learner_id: 1,
course_id: 201,
enrollment_date: ISODate("2026-01-10"),
payment: {
amount: 15000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 8,
total_modules: 10,
completion_percent: 80
},
quiz_scores: [75, 82, 88],
status: "Active"
},
{
enrollment_id: 1002,
learner_id: 2,
course_id: 202,
enrollment_date: ISODate("2026-01-15"),
payment: {
amount: 20000,
mode: "Card",
status: "Success"
},
progress: {
completed_modules: 10,
total_modules: 10,
completion_percent: 100
},
quiz_scores: [90, 92, 95],
status: "Completed"
},
{
enrollment_id: 1003,
learner_id: 3,
course_id: 203,
enrollment_date: ISODate("2026-02-01"),
payment: {
amount: 8000,
mode: "Cash",
status: "Pending"
},
progress: {
completed_modules: 3,
total_modules: 8,
completion_percent: 37.5
},
quiz_scores: [60, 65],
status: "Active"
},
{
enrollment_id: 1004,
learner_id: 4,
course_id: 204,
enrollment_date: ISODate("2026-02-10"),
payment: {
amount: 12000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 6,
total_modules: 12,
completion_percent: 50
},
quiz_scores: [78, 80, 85],
status: "Active"
},
{
enrollment_id: 1005,
learner_id: 5,
course_id: 205,
enrollment_date: ISODate("2026-03-05"),
payment: {
amount: 18000,
mode: "Card",
status: "Failed"
},
progress: {
completed_modules: 0,
total_modules: 12,
completion_percent: 0
},
quiz_scores: [],
status: "Payment Failed"
},
{
enrollment_id: 1006,
learner_id: 6,
course_id: 202,
enrollment_date: ISODate("2026-03-12"),
payment: {
amount: 20000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 2,
total_modules: 10,
completion_percent: 20
},
quiz_scores: [55],
status: "Active"
}
])

// queries


// Query 1
db.learners.find()

// Query 2
db.courses.find()

// Query 3
db.learners.find(
    {},
    {
        name: 1,
        city: 1,
        goal: 1,
        _id: 0
    }
)

// Query 4
db.learners.find({
    city: "Hyderabad"
})

// Query 5
db.learners.find({
    goal: "AI Engineer"
})

// Query 6
db.courses.find({
    category: "Data Engineering"
})

// Query 7
db.courses.find({
    price: { $gt: 10000 }
})

// Query 8
db.courses.find({
    level: "Beginner"
})

// Query 9
db.enrollments.find({
    "payment.status": "Success"
})

// Query 10
db.learners.find({
    phone: null
})

// Query 11
db.learners.find({
    experience_years: { $gt: 2 }
})

// Query 12
db.courses.find({
    price: {
        $gte: 8000,
        $lte: 18000
    }
})

// Query 13
db.courses.find({
    level: {
        $in: ["Beginner", "Intermediate"]
    }
})

// Query 14
db.enrollments.find({
    "progress.completion_percent": {
        $gte: 80
    }
})

// Query 15
db.enrollments.find({
    "payment.status": {
        $ne: "Success"
    }
})

// Query 16
db.learners.find({
    city: {
        $in: ["Hyderabad", "Bangalore", "Pune"]
    }
})

// Query 17
db.courses.find({
    category: {
        $ne: "Cloud"
    }
})

// Query 18
db.instructors.find({
    expertise: "AI"
})

// Query 19
db.instructors.find({
    expertise: "SQL"
})

// Query 20
db.courses.find({
    tools: "Python"
})

// Query 21
db.courses.find({
    tools: "Databricks"
})

// Query 22
db.enrollments.find({
    quiz_scores: 95
})

// Query 23
db.enrollments.find({
    quiz_scores: {
        $elemMatch: { $gt: 85 }
    }
})

// Query 24
db.courses.find().sort({
    price: -1
})

// Query 25
db.courses.find().sort({
    price: -1
}).limit(3)

// Query 26
db.learners.find().sort({
    experience_years: -1
})

// Query 27
db.learners.find().sort({
    experience_years: -1
}).limit(2)

// Query 28
db.instructors.find().sort({
    rating: -1
})


// Query 29
db.learners.updateOne(
    { learner_id: 1 },
    { $set: { city: "Secunderabad" } }
)

// Query 30
db.courses.updateOne(
    { course_id: 203 },
    { $set: { price: 9000 } }
)

// Query 31
db.enrollments.updateOne(
    { enrollment_id: 1006 },
    {
        $set: {
            "progress.completion_percent": 30
        }
    }
)

// Query 32
db.enrollments.updateOne(
    { enrollment_id: 1005 },
    { $set: { status: "Inactive" } }
)

// Query 33
db.learners.updateMany(
    {},
    { $set: { active: true } }
)

// Query 34
db.learners.updateMany(
    {},
    { $unset: { active: "" } }
)

// Query 35
db.courses.updateOne(
    { course_id: 201 },
    { $push: { tools: "MongoDB" } }
)

// Query 36
db.enrollments.deleteMany({
    "payment.status": "Failed"
})

// Query 37
db.learners.deleteMany({
    experience_years: 0
})

// Query 38
db.learners.countDocuments()

// Query 39
db.courses.countDocuments()

// Query 40
db.enrollments.countDocuments({
    "payment.status": "Success"
})

// Query 41
db.learners.distinct("city")

// Query 42
db.courses.distinct("category")

// Query 43
db.enrollments.distinct("payment.mode")

// Query 44
db.enrollments.aggregate([
    {
        $group: {
            _id: "$payment.mode",
            TotalRevenue: {
                $sum: "$payment.amount"
            }
        }
    }
])

// Query 45
db.enrollments.aggregate([
    {
        $group: {
            _id: "$course_id",
            TotalRevenue: {
                $sum: "$payment.amount"
            }
        }
    }
])

// Query 46
db.learners.aggregate([
    {
        $group: {
            _id: "$goal",
            TotalLearners: {
                $sum: 1
            }
        }
    }
])

// Query 47
db.courses.aggregate([
    {
        $group: {
            _id: "$category",
            AverageCoursePrice: {
                $avg: "$price"
            }
        }
    }
])

// Query 48
db.enrollments.aggregate([
    {
        $group: {
            _id: "$course_id",
            AverageCompletionPercent: {
                $avg: "$progress.completion_percent"
            }
        }
    }
])

// Query 49
db.enrollments.aggregate([
    {
        $group: {
            _id: "$status",
            TotalEnrollments: {
                $sum: 1
            }
        }
    }
])

// Query 50
db.enrollments.aggregate([
    {
        $group: {
            _id: "$course_id",
            TotalRevenue: {
                $sum: "$payment.amount"
            }
        }
    },
    {
        $match: {
            TotalRevenue: { $gt: 15000 }
        }
    }
])

// Query 51
db.enrollments.aggregate([
    {
        $lookup: {
            from: "learners",
            localField: "learner_id",
            foreignField: "learner_id",
            as: "learner_details"
        }
    },
    {
        $unwind: "$learner_details"
    },
    {
        $project: {
            _id: 0,
            enrollment_id: 1,
            learner_name: "$learner_details.name",
            city: "$learner_details.city",
            course_id: 1,
            status: 1
        }
    }
])

// Query 52
db.enrollments.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "course_id",
            foreignField: "course_id",
            as: "course_details"
        }
    },
    {
        $unwind: "$course_details"
    },
    {
        $project: {
            _id: 0,
            enrollment_id: 1,
            course_name: "$course_details.course_name",
            category: "$course_details.category",
            amount: "$payment.amount",
            payment_status: "$payment.status"
        }
    }
])

// Query 53
db.courses.aggregate([
    {
        $lookup: {
            from: "instructors",
            localField: "instructor_id",
            foreignField: "instructor_id",
            as: "instructor_details"
        }
    },
    {
        $unwind: "$instructor_details"
    },
    {
        $project: {
            _id: 0,
            course_name: 1,
            category: 1,
            instructor_name: "$instructor_details.instructor_name",
            instructor_rating: "$instructor_details.rating"
        }
    }
])

// Query 54
db.enrollments.aggregate([
    {
        $lookup: {
            from: "learners",
            localField: "learner_id",
            foreignField: "learner_id",
            as: "learner_details"
        }
    },
    {
        $lookup: {
            from: "courses",
            localField: "course_id",
            foreignField: "course_id",
            as: "course_details"
        }
    },
    {
        $unwind: "$learner_details"
    },
    {
        $unwind: "$course_details"
    },
    {
        $lookup: {
            from: "instructors",
            localField: "course_details.instructor_id",
            foreignField: "instructor_id",
            as: "instructor_details"
        }
    },
    {
        $unwind: "$instructor_details"
    },
    {
        $project: {
            _id: 0,
            enrollment_id: 1,
            learner_name: "$learner_details.name",
            city: "$learner_details.city",
            goal: "$learner_details.goal",
            course_name: "$course_details.course_name",
            category: "$course_details.category",
            instructor_name: "$instructor_details.instructor_name",
            payment_amount: "$payment.amount",
            payment_status: "$payment.status",
            completion_percent: "$progress.completion_percent",
            enrollment_status: "$status"
        }
    }
])