from app import create_app, db  
app = create_app()

# force create db at Gunicorn level
with app.app_context():
    try:
        db.create_all()
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating database tables: {e}")

if __name__ == "__main__":
    app.run(debug=True)