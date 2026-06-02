use food_delivery_capstone_db

db.createCollection("customers")
db.createCollection("restaurants")
db.createCollection("delivery_partners")
db.createCollection("orders")

// inserting into collections 

db.customers.insertMany([
{
customer_id: 1,
name: "Rahul Sharma",
city: "Hyderabad",
membership: "Gold",
phone: "9876543210"
},
{
customer_id: 2,
name: "Priya Reddy",
city: "Bangalore",
membership: "Silver",
phone: "9876543211"
},
{
customer_id: 3,
name: "Amit Kumar",
city: "Mumbai",
membership: "Gold",
phone: null
},
{
customer_id: 4,
name: "Sneha Patel",
city: "Chennai",
membership: "Bronze",
phone: "9876543213"
},
{
customer_id: 5,
name: "Arjun Verma",
city: "Delhi",
membership: "Silver",
phone: "9876543214"
}
])

db.restaurants.insertMany([
{
restaurant_id: 101,
name: "Spice Hub",
city: "Hyderabad",
cuisine: "Indian",
rating: 4.5
},
{
restaurant_id: 102,
name: "Pizza Corner",
city: "Bangalore",
cuisine: "Italian",
rating: 4.2
},
{
restaurant_id: 103,
name: "Green Bowl",
city: "Chennai",
cuisine: "Healthy",
rating: 4.7
},
{
restaurant_id: 104,
name: "Burger Street",
city: "Mumbai",
cuisine: "Fast Food",
rating: 3.9
},
{
restaurant_id: 105,
name: "Royal Tandoor",
city: "Delhi",
cuisine: "Indian",
rating: 4.8
}
])

db.delivery_partners.insertMany([
{
partner_id: 201,
partner_name: "FastMove Logistics",
city: "Hyderabad",
rating: 4.4
},
{
partner_id: 202,
partner_name: "QuickShip",
city: "Bangalore",
rating: 4.1
},
{
partner_id: 203,
partner_name: "SpeedKart",
city: "Mumbai",
rating: 4.6
},
{
partner_id: 204,
partner_name: "DoorDash India",
city: "Delhi",
rating: 4.0
}
])

db.orders.insertMany([
{
order_id: 1001,
customer_id: 1,
restaurant_id: 101,
partner_id: 201,
items: [
{ item_name: "Biryani", quantity: 2, price: 250 },
{ item_name: "Kebab", quantity: 1, price: 180 }
],
order_amount: 680,
payment: {
mode: "UPI",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 35,
order_rating: 5
},
{
order_id: 1002,
customer_id: 2,
restaurant_id: 102,
partner_id: 202,
items: [
{ item_name: "Pizza", quantity: 1, price: 500 },
{ item_name: "Garlic Bread", quantity: 1, price: 150 }
],
order_amount: 650,
payment: {
mode: "Card",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 42,
order_rating: 4
},
{
order_id: 1003,
customer_id: 3,
restaurant_id: 104,
partner_id: 203,
items: [
{ item_name: "Burger", quantity: 2, price: 180 },
{ item_name: "Fries", quantity: 1, price: 120 }
],
order_amount: 480,
payment: {
mode: "Cash",
status: "Pending"
},
order_status: "Pending",
delivery_time_minutes: null,
order_rating: null
},
{
order_id: 1004,
customer_id: 4,
restaurant_id: 103,
partner_id: null,
items: [
{ item_name: "Salad Bowl", quantity: 1, price: 350 }
],
order_amount: 350,
payment: {
mode: "UPI",
status: "Failed"
},
order_status: "Cancelled",
delivery_time_minutes: null,
order_rating: null
},
{
order_id: 1005,
customer_id: 5,
restaurant_id: 105,
partner_id: 204,
items: [
{ item_name: "Tandoori Chicken", quantity: 1, price: 600 },
{ item_name: "Naan", quantity: 2, price: 60 }
],
order_amount: 720,
payment: {
mode: "UPI",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 50,
order_rating: 5
},
{
order_id: 1006,
customer_id: 1,
restaurant_id: 101,
partner_id: 201,
items: [
{ item_name: "Paneer Curry", quantity: 1, price: 300 },
{ item_name: "Roti", quantity: 4, price: 25 }
],
order_amount: 400,
payment: {
mode: "Card",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 30,
order_rating: 4
}
])


// Query 1
db.customers.find()

// Query 2
db.restaurants.find()

// Query 3
db.customers.find(
    {},
    {
        name: 1,
        city: 1,
        membership: 1,
        _id: 0
    }
)

// Query 4
db.customers.find({
    city: "Hyderabad"
})

// Query 5
db.customers.find({
    membership: "Gold"
})

// Query 6
db.restaurants.find({
    rating: { $gt: 4.5 }
})

// Query 7
db.orders.find({
    order_amount: { $gt: 500 }
})

// Query 8
db.orders.find({
    order_status: "Delivered"
})

// Query 9
db.orders.find({
    order_status: "Cancelled"
})

// Query 10
db.customers.find({
    phone: null
})

// Query 11
db.orders.find({
    order_amount: {
        $gte: 400,
        $lte: 700
    }
})

// Query 12
db.customers.find({
    city: {
        $in: ["Hyderabad", "Delhi", "Mumbai"]
    }
})

// Query 13
db.restaurants.find({
    cuisine: {
        $in: ["Indian", "Fast Food"]
    }
})

// Query 14
db.orders.find({
    "payment.status": {
        $ne: "Success"
    }
})

// Query 15
db.orders.find({
    delivery_time_minutes: null
})

// Query 16
db.orders.find({
    order_rating: {
        $gte: 4
    }
})

// Query 17
db.restaurants.find({
    city: {
        $nin: ["Bangalore", "Chennai"]
    }
})

// Query 18
db.orders.find({
    "items.item_name": "Biryani"
})

// Query 19
db.orders.find({
    "items.item_name": "Pizza"
})

// Query 20
db.orders.find({
    items: {
        $elemMatch: {
            quantity: { $gt: 1 }
        }
    }
})

// Query 21
db.orders.find({
    items: {
        $elemMatch: {
            price: { $gt: 300 }
        }
    }
})

// Query 22
db.orders.find(
    {},
    {
        order_id: 1,
        items: 1,
        _id: 0
    }
)

// Query 23
db.restaurants.find().sort({
    rating: -1
})

// Query 24
db.restaurants.find().sort({
    rating: -1
}).limit(3)

// Query 25
db.orders.find().sort({
    order_amount: -1
})

// Query 26
db.orders.find().sort({
    order_amount: -1
}).limit(2)

// Query 27
db.delivery_partners.find().sort({
    rating: -1
})

// Query 28
db.customers.updateOne(
    { customer_id: 1 },
    { $set: { membership: "Platinum" } }
)

// Query 29
db.restaurants.updateOne(
    { restaurant_id: 104 },
    { $set: { rating: 4.1 } }
)

// Query 30
db.orders.updateOne(
    { order_id: 1003 },
    { $set: { order_status: "Delivered" } }
)

// Query 31
db.orders.updateOne(
    { order_id: 1003 },
    { $set: { delivery_time_minutes: 45 } }
)

// Query 32
db.customers.updateMany(
    {},
    { $set: { active: true } }
)

// Query 33
db.customers.updateMany(
    {},
    { $unset: { active: "" } }
)

// Query 34
db.orders.updateOne(
    { order_id: 1006 },
    {
        $push: {
            items: {
                item_name: "Curd Rice",
                quantity: 1,
                price: 120
            }
        }
    }
)

// Query 35
db.orders.deleteMany({
    order_status: "Cancelled"
})

// Query 36
db.restaurants.deleteMany({
    rating: { $lt: 4.0 }
})

// Query 37
db.customers.countDocuments()

// Query 38
db.orders.countDocuments()

// Query 39
db.orders.countDocuments({
    order_status: "Delivered"
})

// Query 40
db.orders.countDocuments({
    "payment.status": "Failed"
})

// Query 41
db.customers.distinct("city")

// Query 42
db.restaurants.distinct("cuisine")

// Query 43
db.orders.distinct("payment.mode")

// Query 44
db.orders.aggregate([
    {
        $group: {
            _id: "$payment.mode",
            TotalRevenue: {
                $sum: "$order_amount"
            }
        }
    }
])

// Query 45
db.orders.aggregate([
    {
        $group: {
            _id: "$order_status",
            TotalRevenue: {
                $sum: "$order_amount"
            }
        }
    }
])

// Query 46
db.orders.aggregate([
    {
        $match: {
            order_status: "Delivered"
        }
    },
    {
        $group: {
            _id: null,
            AverageDeliveryTime: {
                $avg: "$delivery_time_minutes"
            }
        }
    }
])

// Query 47
db.orders.aggregate([
    {
        $group: {
            _id: "$customer_id",
            TotalOrders: {
                $sum: 1
            },
            TotalAmount: {
                $sum: "$order_amount"
            }
        }
    }
])

// Query 48
db.orders.aggregate([
    {
        $group: {
            _id: "$restaurant_id",
            TotalOrders: {
                $sum: 1
            },
            TotalRevenue: {
                $sum: "$order_amount"
            }
        }
    }
])

// Query 49
db.orders.aggregate([
    {
        $match: {
            order_rating: { $ne: null }
        }
    },
    {
        $group: {
            _id: "$restaurant_id",
            AverageRating: {
                $avg: "$order_rating"
            }
        }
    }
])

// Query 50
db.orders.aggregate([
    {
        $group: {
            _id: "$customer_id",
            TotalSpending: {
                $sum: "$order_amount"
            }
        }
    },
    {
        $match: {
            TotalSpending: { $gt: 700 }
        }
    }
])

// Query 51
db.orders.aggregate([
    {
        $lookup: {
            from: "customers",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "customer_details"
        }
    },
    {
        $unwind: "$customer_details"
    },
    {
        $project: {
            _id: 0,
            order_id: 1,
            customer_name: "$customer_details.name",
            city: "$customer_details.city",
            order_amount: 1,
            order_status: 1
        }
    }
])

// Query 52
db.orders.aggregate([
    {
        $lookup: {
            from: "restaurants",
            localField: "restaurant_id",
            foreignField: "restaurant_id",
            as: "restaurant_details"
        }
    },
    {
        $unwind: "$restaurant_details"
    },
    {
        $project: {
            _id: 0,
            order_id: 1,
            restaurant_name: "$restaurant_details.name",
            cuisine: "$restaurant_details.cuisine",
            order_amount: 1
        }
    }
])

// Query 53
db.orders.aggregate([
    {
        $lookup: {
            from: "delivery_partners",
            localField: "partner_id",
            foreignField: "partner_id",
            as: "partner_details"
        }
    },
    {
        $unwind: "$partner_details"
    },
    {
        $project: {
            _id: 0,
            order_id: 1,
            partner_name: "$partner_details.partner_name",
            delivery_time_minutes: 1,
            order_status: 1
        }
    }
])

// Query 54
db.orders.aggregate([
    {
        $lookup: {
            from: "customers",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "customer_details"
        }
    },
    {
        $lookup: {
            from: "restaurants",
            localField: "restaurant_id",
            foreignField: "restaurant_id",
            as: "restaurant_details"
        }
    },
    {
        $lookup: {
            from: "delivery_partners",
            localField: "partner_id",
            foreignField: "partner_id",
            as: "partner_details"
        }
    },
    {
        $unwind: "$customer_details"
    },
    {
        $unwind: "$restaurant_details"
    },
    {
        $unwind: {
            path: "$partner_details",
            preserveNullAndEmptyArrays: true
        }
    },
    {
        $project: {
            _id: 0,
            order_id: 1,
            customer_name: "$customer_details.name",
            restaurant_name: "$restaurant_details.name",
            cuisine: "$restaurant_details.cuisine",
            partner_name: "$partner_details.partner_name",
            order_amount: 1,
            payment_mode: "$payment.mode",
            payment_status: "$payment.status",
            order_status: 1,
            delivery_time_minutes: 1,
            order_rating: 1
        }
    }
])

