// server.js
const express = require('express');
const app = express();
const PORT = 3000;

// Mock job list for now
const jobs = [
  { title: "SSC GD Constable 2025", link: "https://ssc.nic.in/" },
  { title: "UPSC Civil Services 2025", link: "https://upsc.gov.in/" },
];

app.get('/api/jobs', (req, res) => {
  res.json(jobs);
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
