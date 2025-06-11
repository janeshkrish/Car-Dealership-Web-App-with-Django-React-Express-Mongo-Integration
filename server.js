const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb+srv://expressUser:<db_password>@cluster0.bpj6dkk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log("MongoDB connected"))
  .catch(err => console.log(err));

// Schemas
const ReviewSchema = new mongoose.Schema({
  reviewer: String,
  comment: String,
  rating: Number
});

const DealerSchema = new mongoose.Schema({
  name: String,
  state: String,
  reviews: [ReviewSchema]
});

const Dealer = mongoose.model("Dealer", DealerSchema);

// Routes

// All dealerships
app.get('/dealerships', async (req, res) => {
  const dealers = await Dealer.find();
  res.json(dealers);
});

// Dealer by ID
app.get('/dealer/:id', async (req, res) => {
  try {
    const dealer = await Dealer.findById(req.params.id);
    res.json(dealer);
  } catch (err) {
    res.status(404).json({ message: 'Dealer not found' });
  }
});

// Dealer reviews by ID
app.get('/dealer/:id/reviews', async (req, res) => {
  try {
    const dealer = await Dealer.findById(req.params.id);
    res.json(dealer.reviews);
  } catch (err) {
    res.status(404).json({ message: 'Dealer not found' });
  }
});

// Dealers by state (e.g., Kansas)
app.get('/dealers/Kansas', async (req, res) => {
  const dealers = await Dealer.find({ state: 'Kansas' });
  res.json(dealers);
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
