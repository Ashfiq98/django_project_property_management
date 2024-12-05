# Django Property Management System

## Project Overview

This is a Django-based Property Management System that provides a robust solution for managing property information with geospatial support. The project uses PostgreSQL with PostGIS extensions for advanced location and property data handling.

## Key Features

- Admin interface for comprehensive property management
- Geospatial data support with PostGIS
- User groups with role-based access control
- Property owners can manage their own properties
- Localized accommodation descriptions
- CSV import functionality for location data

## Prerequisites

- Docker
- Postgress Sql
- Docker Compose
- Git

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ashfiq98/django_project_property_management.git
cd django_project_property_management/inventory_management
code . ## for opening inside vs code
```

### 2. Environment Configuration

1. Ensure Docker and Docker Compose are installed on your system
2. Make virtual environment
   ```bash
   python -m venv venv
   ```
   For Linux/MacOS:
   ```bash
   source venv/bin/activate
   ```
   For Windows:
   ```bash
   venv\Scripts\activate
   ```

### 3. Build and Run with Docker
* Open termninal & : 
```bash
# Build the Docker containers
docker-compose build

# Start the services
docker-compose up -d

# Run database migrations
docker-compose exec web python manage.py migrate

# Create a superuser (follow the prompts)
docker-compose exec web python manage.py createsuperuser
```

### 4. Accessing the Application

- Web Application: `http://localhost:8000`
- Admin Interface: `http://localhost:8000/admin`
  - Use the superuser credentials created in step 3
 
### 5. For creating property Owners group:
- After login as admin inside this link : `http://localhost:8000/admin`
- Manually create a group , for example : 'property_owners'
- Then give them permission to these :
  * Properties | accomodation | Can add accomodation
  * Properties | accomodation | Can change accomodation
  * Properties | accomodation | Can delete accomodation
  * Properties | accomodation | Can view accomodation
  * Properties | location | Can view location
     (without giving the permission of view location, user could't access the location dropdown field, that's why i 
      gave this permission)


## Project Structure

- **Models**:
  - `Location`: Handles hierarchical location data with geospatial support
  - `Accommodation`: Stores property details with geolocation
  - `LocalizeAccommodation`: Provides localized property descriptions

## User Roles and Permissions

- **Admin**:
  - Full access to all data
  - Can add accommodations, locations, users, and groups
  - Manages system-wide configurations
  - If the admin grants staff status to a user, the user will be able to log in and view their own accommodations.

- **Property Owners**:
  - Can only view, add, edit, and delete their own accommodations
  - Cannot see other users' properties

## Additional Features

- CSV Import: Location data can be imported through the Django Admin interface
- Geospatial Support: Leverages PostGIS for advanced location-based queries

### Data Import Instructions
1. Login as admin
2. Navigate to the locations section
3. Click on import
4. Select the prepared CSV file
5. Confirm the data import

### Dummy Data Examples

####  Location Data
 csv
id,title,location_type,country_code,state_abbr,city
LOC001,San Francisco,city,US,CA,San Francisco
LOC002,Singapore City,city,SG,SG,Singapore
LOC003,Sydney Metro,city,AU,NSW,Sydney

# Generate sitemap using Docker
docker-compose exec web bash
python manage.py generate_sitemap

### Running Tests

```bash
# Run unit tests
docker-compose exec web python manage.py test

# Check test coverage
docker-compose exec web coverage run --source='.' manage.py test
docker-compose exec web coverage report
```

## Deployment Considerations

- Ensure all environment variables are properly configured
- Set `DEBUG=0` in production
- Use strong, unique `SECRET_KEY`
- Configure proper database credentials

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

