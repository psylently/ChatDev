const express = require('express');
const multer = require('multer');
const { LibreTranslateAPI } = require('libretranslate');
const fs = require('fs');
const app = express();
const upload = multer({ dest: 'uploads/' });
const translator = new LibreTranslateAPI();
app.post('/translate', upload.single('file'), (req, res) => {
  const filePath = req.file.path;
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: 'Internal server error' });
    } else {
      translator.translate(data, 'en', 'fr')
        .then((translatedText) => {
          res.json({ translatedText });
        })
        .catch((error) => {
          console.error(error);
          res.status(500).json({ error: 'Internal server error' });
        });
    }
  });
});
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});