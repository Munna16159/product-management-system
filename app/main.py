from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "FastAPI with MySQL is working!"}


@app.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@app.get("/products/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Deleted successfully"}

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = updated_product.name
    product.description = updated_product.description
    product.quantity = updated_product.quantity
    product.price = updated_product.price

    db.commit()
    db.refresh(product)

    return product