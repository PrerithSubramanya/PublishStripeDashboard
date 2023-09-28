# Streamlit Stripe Terminal Locations App

This Streamlit app interfaces with the Stripe API to fetch details of terminal locations based on the given location ID.

## Prerequisites

- Python 3.x
- Streamlit
- Requests library

## Setup

1. Clone this repository:

   ```
   git clone [your-repository-url]
   ```

2. Navigate to the project directory:

   ```
   cd [your-directory-name]
   ```

3. Install the required packages:

   ```
   pip install streamlit requests
   ```

4. Set up the Streamlit secrets:

   - Create a `.streamlit` directory in the project root.
   - Inside the `.streamlit` directory, create a `secrets.toml` file.
   - Add the following content to the `secrets.toml` file:

   ```toml
   [secrets]
   api_key = "your_stripe_api_key_here"
   device_group_key = "your_device_group_key_here"
   device_group_value = "your_device_group_value_here"
   ```

   Make sure to replace placeholders with your actual Stripe API key and other values.

## Running the App

To run the app, use the following command:

```
streamlit run stripe_app.py
```

Your browser should open automatically, and you can interact with the Streamlit app.

