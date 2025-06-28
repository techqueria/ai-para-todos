"""
Iris Dataset EDA + Machine Learning - Versión Simplificada
AI Para Todos - Vibe Coding Workshop
Cursor AI Advanced Coding Project

Este proyecto demuestra análisis de datos y machine learning básico con el dataset Iris.
This project demonstrates basic data analysis and machine learning with the Iris dataset.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

class IrisAnalyzer:
    """
    Clase para análisis básico de datos y machine learning con el dataset Iris
    Class for basic data analysis and machine learning with the Iris dataset
    """
    
    def __init__(self):
        """Inicializar el analizador de datos"""
        self.data = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        
    def load_data(self):
        """
        Cargar el dataset Iris desde sklearn
        Load Iris dataset from sklearn
        """
        print("🌱 Cargando dataset Iris...")
        print("Loading Iris dataset...")
        
        from sklearn.datasets import load_iris
        iris = load_iris()
        
        # Crear DataFrame con los datos
        # Create DataFrame with the data
        self.data = pd.DataFrame(
            data=np.c_[iris['data'], iris['target']],
            columns=iris['feature_names'] + ['target']
        )
        
        # Mapear los números de target a nombres de especies
        # Map target numbers to species names
        target_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        self.data['species'] = self.data['target'].map(target_names)
        
        print(f"✅ Dataset cargado con {len(self.data)} filas y {len(self.data.columns)} columnas")
        print(f"✅ Dataset loaded with {len(self.data)} rows and {len(self.data.columns)} columns")
        
        return self.data
    
    def explore_data(self):
        """
        Análisis exploratorio de datos básico
        Basic exploratory data analysis
        """
        print("\n📊 ANÁLISIS EXPLORATORIO DE DATOS")
        print("📊 EXPLORATORY DATA ANALYSIS")
        print("=" * 50)
        
        # Información básica del dataset
        # Basic dataset information
        print("\n1. Información del Dataset / Dataset Information:")
        print(f"   Filas / Rows: {len(self.data)}")
        print(f"   Columnas / Columns: {len(self.data.columns)}")
        print(f"   Tipos de datos / Data types: {self.data.dtypes.unique()}")
        
        print("\n2. Primeras 5 filas / First 5 rows:")
        print(self.data.head())
        
        print("\n3. Estadísticas descriptivas / Descriptive statistics:")
        print(self.data.describe())
        
        print("\n4. Distribución de especies / Species distribution:")
        print(self.data['species'].value_counts())
        
        # Verificar valores faltantes
        # Check for missing values
        print("\n5. Valores faltantes / Missing values:")
        print(self.data.isnull().sum())
    
    def prepare_data_for_ml(self):
        """
        Preparar datos para machine learning
        Prepare data for machine learning
        """
        print("\n🤖 PREPARANDO DATOS PARA MACHINE LEARNING")
        print("🤖 PREPARING DATA FOR MACHINE LEARNING")
        print("=" * 50)
        
        # Separar características y target
        # Separate features and target
        features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
        self.X = self.data[features]
        self.y = self.data['target']
        
        # Dividir en entrenamiento y prueba
        # Split into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        print(f"✅ Datos de entrenamiento: {self.X_train.shape[0]} muestras")
        print(f"✅ Training data: {self.X_train.shape[0]} samples")
        print(f"✅ Datos de prueba: {self.X_test.shape[0]} muestras")
        print(f"✅ Test data: {self.X_test.shape[0]} samples")
        
        print(f"\n📋 Características utilizadas / Features used:")
        for i, feature in enumerate(features, 1):
            print(f"   {i}. {feature}")
    
    def train_model(self):
        """
        Entrenar modelo de machine learning
        Train machine learning model
        """
        print("\n🎯 ENTRENANDO MODELO")
        print("🎯 TRAINING MODEL")
        print("=" * 50)
        
        # Crear y entrenar modelo Random Forest
        # Create and train Random Forest model
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        
        print("✅ Modelo entrenado exitosamente")
        print("✅ Model trained successfully")
        
        # Mostrar importancia de características
        # Show feature importance
        feature_importance = pd.DataFrame({
            'feature': self.X.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\n📊 Importancia de características / Feature importance:")
        print(feature_importance)
    
    def evaluate_model(self):
        """
        Evaluar el modelo entrenado
        Evaluate the trained model
        """
        print("\n📈 EVALUANDO MODELO")
        print("📈 EVALUATING MODEL")
        print("=" * 50)
        
        # Predicciones
        # Predictions
        y_pred = self.model.predict(self.X_test)
        
        # Precisión
        # Accuracy
        accuracy = accuracy_score(self.y_test, y_pred)
        print(f"✅ Precisión del modelo: {accuracy:.4f} ({accuracy*100:.2f}%)")
        print(f"✅ Model accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
        
        # Reporte de clasificación
        # Classification report
        print("\n📊 Reporte de clasificación / Classification report:")
        target_names = ['setosa', 'versicolor', 'virginica']
        print(classification_report(self.y_test, y_pred, target_names=target_names))
    
    def make_predictions(self, sample_data):
        """
        Hacer predicciones con nuevos datos
        Make predictions with new data
        """
        print("\n🔮 HACIENDO PREDICCIONES")
        print("🔮 MAKING PREDICTIONS")
        print("=" * 50)
        
        # Predicción
        # Prediction
        prediction = self.model.predict(sample_data)
        probabilities = self.model.predict_proba(sample_data)
        
        target_names = ['setosa', 'versicolor', 'virginica']
        
        print(f"📊 Datos de entrada / Input data:")
        print(sample_data)
        print(f"\n🎯 Predicción / Prediction: {target_names[int(prediction[0])]}")
        print(f"📈 Probabilidades / Probabilities:")
        for i, prob in enumerate(probabilities[0]):
            print(f"   {target_names[i]}: {prob:.4f} ({prob*100:.2f}%)")
        
        return prediction, probabilities

def main():
    """
    Función principal para ejecutar el análisis completo
    Main function to run the complete analysis
    """
    print("🌺 IRIS DATASET EDA + MACHINE LEARNING - VERSIÓN SIMPLIFICADA")
    print("🌺 AI Para Todos - Vibe Coding Workshop")
    print("=" * 60)
    
    # Crear instancia del analizador
    # Create analyzer instance
    analyzer = IrisAnalyzer()
    
    # Ejecutar análisis completo
    # Run complete analysis
    analyzer.load_data()
    analyzer.explore_data()
    analyzer.prepare_data_for_ml()
    analyzer.train_model()
    analyzer.evaluate_model()
    
    # Ejemplo de predicción
    # Example prediction
    print("\n" + "="*60)
    print("🧪 EJEMPLO DE PREDICCIÓN / PREDICTION EXAMPLE")
    print("="*60)
    
    # Datos de ejemplo (setosa)
    # Example data (setosa)
    sample_data = pd.DataFrame({
        'sepal length (cm)': [5.1],
        'sepal width (cm)': [3.5],
        'petal length (cm)': [1.4],
        'petal width (cm)': [0.2]
    })
    
    analyzer.make_predictions(sample_data)
    
    print("\n🎉 ¡Análisis completado exitosamente!")
    print("🎉 Analysis completed successfully!")
    print("\n💡 Lo que aprendiste / What you learned:")
    print("   - Carga y exploración de datos / Data loading and exploration")
    print("   - Preparación de datos para ML / Data preparation for ML")
    print("   - Entrenamiento de modelos / Model training")
    print("   - Evaluación de modelos / Model evaluation")
    print("   - Hacer predicciones / Making predictions")

if __name__ == "__main__":
    main() 