from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Car(BaseModel):
    id : int
    mark: Optional[str] = None
    model: Optional[str] = None
    body_type: Optional[str] = None
    release_year: Optional[int] = None
    engine_power: Optional[int] = None
    drive_type: Optional[str] = None
    favorite_flag : Optional[bool] = None

# Список машин
repoCars = [
    Car(id = 1, mark="BMW", model="M5 E60", body_type="Седан", release_year=2007, engine_power=560, drive_type="RWD", favorite_flag=True),
    Car(id = 2, mark="Audi", model="RS6 C7", body_type="Универсал", release_year=2016, engine_power=605, drive_type="AWD", favorite_flag=True),
    Car(id = 3, mark="Mercedes", model="E63 AMG", body_type="Седан", release_year=2018, engine_power=612, drive_type="AWD"),
    Car(id = 4, mark="Tesla", model="Model 3", body_type="Седан", release_year=2021, engine_power=450, drive_type="AWD"),
    Car(id = 5, mark="Toyota", model="Supra", body_type="Купе", release_year=2020, engine_power=340, drive_type="RWD"),
    Car(id = 6, mark="Nissan", model="GT-R R35", body_type="Купе", release_year=2019, engine_power=565, drive_type="AWD"),
    Car(id = 7, mark="Porsche", model="911 Turbo S", body_type="Купе", release_year=2022, engine_power=650, drive_type="AWD"),
    Car(id = 8, mark="Chevrolet", model="Camaro ZL1", body_type="Купе", release_year=2017, engine_power=650, drive_type="RWD"),
    Car(id = 9, mark="Ford", model="Mustang GT", body_type="Купе", release_year=2022, engine_power=450, drive_type="RWD"),
    Car(id = 10, mark="Lamborghini", model="Huracan", body_type="Купе", release_year=2021, engine_power=640, drive_type="AWD"),
    Car(id = 11, mark="Ferrari", model="F8 Tributo", body_type="Купе", release_year=2020, engine_power=720, drive_type="RWD"),
    Car(id = 12, mark="McLaren", model="721S", body_type="Купе", release_year=2019, engine_power=720, drive_type="RWD"),
    Car(id = 13, mark="Jaguar", model="F-Type", body_type="Купе", release_year=2021, engine_power=575, drive_type="AWD"),
    Car(id = 14, mark="Alfa Romeo", model="Giulia Quadrifoglio", body_type="Седан", release_year=2021, engine_power=505, drive_type="RWD"),
    Car(id = 15, mark="Dodge", model="Charger SRT Hellcat", body_type="Седан", release_year=2020, engine_power=717, drive_type="RWD"),
    Car(id = 16, mark="Maserati", model="Ghibli Trofeo", body_type="Седан", release_year=2022, engine_power=580, drive_type="RWD"),
    Car(id = 17, mark="Bentley", model="Continental GT", body_type="Купе", release_year=2021, engine_power=626, drive_type="AWD"),
    Car(id = 18, mark="Aston Martin", model="Vantage", body_type="Купе", release_year=2022, engine_power=528, drive_type="RWD"),
    Car(id = 19, mark="Rolls-Royce", model="Ghost", body_type="Седан", release_year=2021, engine_power=563, drive_type="AWD"),
    Car(id = 20, mark="Bugatti", model="Chiron", body_type="Купе", release_year=2022, engine_power=1500, drive_type="AWD")
]

@app.get("/cars", response_model=list[Car])
def get_cars():
    return repoCars

@app.get("/cars/{id}", response_model = Car)
def get_cars_id(id: int):
    for o in repoCars:
        if o.id == id:
            return o
        
@app.get("/favorite", response_model= list[Car])
def get_favirite_cars():
    favorite_repo = []
    for o in repoCars:
        if o.favorite_flag == True:
            favorite_repo.append(o)
    return favorite_repo 

@app.delete("/cars/{id}", response_model = Car)
def delete_book(id : int):
    for o in repoCars:
        if o.id == id:
            repoCars.remove(o)
            return 
    return

@app.post("/cars",response_model = Car)
def add_car(data: Car):
    repoCars.append(data)
    return data


@app.put("/cars/{id}", response_model=Car)
def update_car(id: int, data: Car):
    for o in repoCars:
        if o.id == id:
            if data.mark:
                o.mark = data.mark
            if data.model:
                o.model = data.model
            if data.body_type:
                o.body_type = data.body_type
            if data.release_year:
                o.release_year = data.release_year
            if data.engine_power:
                o.engine_power = data.engine_power
            if data.drive_type:
                o.drive_type = data.drive_type
            if data.favorite_flag is not None:
                o.favorite_flag = data.favorite_flag
            return o
    return {"message": "Авто не найдено"}