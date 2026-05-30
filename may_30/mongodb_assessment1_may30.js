question1

db.restaurants.find()

question2

db.restaurants.find(
    {},
    { name: 1, city: 1, cuisine: 1, _id: 0 }
)

question3

db.restaurants.find({
    city: "Hyderabad"
})

question4

db.restaurants.find({
    cuisine: "Indian"
})

question5

db.restaurants.find({
    delivery_available: true
})

question6

db.restaurants.find({
    rating: { $gt: 4.5 }
})

question7

db.restaurants.find({
    avg_order_value: { $lt: 400 }
})

question8

db.restaurants.find({
    rating: { $gte: 4.0, $lte: 4.7 }
})

question9

db.restaurants.find({
    avg_order_value: { $gte: 600 }
})

question10

db.restaurants.find({
    city: "Hyderabad",
    delivery_available: true
})

question11

db.restaurants.find({
    $or: [
        { city: "Chennai" },
        { cuisine: "Indian" }
    ]
})

question12

db.restaurants.find({
    delivery_available: false
})

question13

db.restaurants.find({
    city: { $in: ["Hyderabad", "Delhi", "Mumbai"] }
})

question14

db.restaurants.find({
    cuisine: { $in: ["Indian", "Italian", "Cafe"] }
})

question15

db.restaurants.find({
    city: { $nin: ["Hyderabad", "Bangalore"] }
})

question16

db.restaurants.find({
    name: /^P/
})

question17

db.restaurants.find({
    name: /Point/
})

question18

db.restaurants.find({
    cuisine: /Food/
})

question19

db.restaurants.find({
    "contact.phone": null
})

question20

db.restaurants.find({
    "contact.email": null
})

question21

db.restaurants.find({
    $or: [
        { "contact.phone": null },
        { "contact.email": null }
    ]
})

question22

db.restaurants.find({
    tags: "premium"
})

question23

db.restaurants.find({
    tags: "fast food"
})

question24

db.restaurants.find({
    tags: {
        $all: ["north indian", "premium"]
    }
})

question25

db.restaurants.find().sort({
    rating: -1
})


question26

db.restaurants.find().sort({
    rating: -1
}).limit(3)

question27

db.restaurants.find().sort({
    avg_order_value: 1
})

question28

db.restaurants.find().sort({
    avg_order_value: -1
}).limit(2)

question29

db.restaurants.updateOne(
    { name: "Burger Street" },
    { $set: { rating: 4.0 } }
)

question30

db.restaurants.updateOne(
    { name: "Tea Tales" },
    { $set: { delivery_available: true } }
)

question31

db.restaurants.updateMany(
    {},
    { $set: { active: true } }
)

question32

db.restaurants.updateOne(
    { name: "Spice Hub" },
    { $push: { tags: "popular" } }
)

question33

db.restaurants.updateMany(
    {},
    { $unset: { active: "" } }
)

question34

db.restaurants.deleteOne({
    restaurant_id: 6
})

question35

db.restaurants.deleteMany({
    rating: { $lt: 4.0 }
})

question36

db.restaurants.countDocuments()

question37

db.restaurants.countDocuments({
    delivery_available: true
})

question38

db.restaurants.distinct("city")

question39

db.restaurants.distinct("cuisine")

question40

db.restaurants.aggregate([
    {
        $group: {
            _id: "$city",
            restaurantCount: { $sum: 1 }
        }
    }
])

question41

db.restaurants.aggregate([
    {
        $group: {
            _id: "$cuisine",
            restaurantCount: { $sum: 1 }
        }
    }
])

question42

db.restaurants.aggregate([
    {
        $group: {
            _id: "$cuisine",
            averageRating: { $avg: "$rating" }
        }
    }
])

question43

db.restaurants.aggregate([
    {
        $group: {
            _id: "$city",
            averageOrderValue: { $avg: "$avg_order_value" }
        }
    }
])

question44

db.restaurants.aggregate([
    {
        $group: {
            _id: "$cuisine",
            highestAverageOrderValue: { $avg: "$avg_order_value" }
        }
    },
    {
        $sort: {
            highestAverageOrderValue: -1
        }
    }
])

question45

db.restaurants.aggregate([
    {
        $group: {
            _id: "$cuisine",
            restaurantCount: { $sum: 1 }
        }
    },
    {
        $match: {
            restaurantCount: { $gt: 1 }
        }
    }
])