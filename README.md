# IMG2Sketch Image to Sketch App Using Flask and OpenCV

![Sketch Image](https://blogger.googleusercontent.com/img/a/AVvXsEh-TNuB0EFfS00gJYh9wkzlM4vnp975MMV8ZymNFlfvZZSOvrkAf6bee1iA9JfzQcIU9Nn4tCGtoy-QRYXwywhCFhvT77lWWHW1RGlQASvmwZGhlmc21ueXQOfGyzeDIsixgdemkm7BM4z41Z5iJ2DhYRNZfozgyoP9w41ZUGahOUBAGb3jMhizRUuhtsud)

## Description

IMG2Sketch is a web application that allows you to convert your images into sketch-style images. It uses Flask as a web framework and OpenCV for image processing. With IMG2Sketch, you can easily transform your photos into artistic sketches.

## Demo

Check out the demo video on YouTube:
[Watch Demo on YouTube](https://youtu.be/VqJFmoTO_Hw?si=hMKkIdfFn35v8Jqv)

Also, see the LinkedIn post for more information:
[LinkedIn Post](https://www.linkedin.com/posts/rohit-ingle-ai_codeclause-opencv-python-activity-7105824581826834432-ukuH?utm_source=share&utm_medium=member_desktop)

## How to Run

Follow these steps to run the IMG2Sketch application:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/IMG2Sketch.git

2. Navigate to the project directory:

   ```bash
   cd IMG2Sketch

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt

4. Run the application:

   ```bash
   python app.py

5. Open your web browser and go to http://localhost:5000.

Usage
1. Visit the IMG2Sketch website using the provided link.
2. Click on the "Choose File" button to upload an image that you want to convert into a sketch.
3. Click the "Submit" button to initiate the sketch conversion process.
4. Wait for the processing to complete. The original image and the resulting sketch will be displayed on the page.
5. You can download the resulting sketch image by clicking on the "Download Sketch" button.

Configuration
The application is configured to allow image uploads with the following file extensions: jpg, jpeg, png, and gif. You can change this configuration by modifying the ALLOWED_EXTENSIONS variable in the app.py file.

Scheduled Cleaning
The application includes a background task that clears the 'uploads' and 'results' folders every 20 minutes to manage storage space. This task is handled by the BackgroundScheduler from the apscheduler library.

Support and Feedback
If you encounter any issues or have suggestions for improvements, please feel free to create an issue on the GitHub repository.

Thank you for using IMG2Sketch!
