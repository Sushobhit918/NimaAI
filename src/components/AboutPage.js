import React from 'react';

function AboutPage() {
  return (
    <section className="about">
      <div className="container">
        <h2>About Nima AI</h2>
        
        <div className="about-content">
          <div className="about-section">
            <h3>Our Mission</h3>
            <p>
              Every year, millions of people worldwide suffer from food allergies, 
              some of which lead to life-threatening reactions such as anaphylaxis. 
              The biggest challenge for individuals with allergies is identifying 
              hidden allergens in packaged foods, restaurant meals, and online orders.
            </p>
            <p>
              Nima AI's mission is to empower individuals with food allergies by 
              providing real-time allergen detection and personalized dietary insights.
            </p>
          </div>
          
          <div className="about-section">
            <h3>The Challenge</h3>
            <h4>Complex Ingredient Terminology</h4>
            <p>
              Food labels often use technical or scientific names for ingredients, 
              making it difficult for consumers to recognize allergens. For example, 
              "Casein" instead of just "Milk" or "Albumin" instead of "Egg protein."
            </p>
            
            <h4>Inconsistent Labeling Standards</h4>
            <p>
              Different countries and brands follow varying food labeling regulations, 
              making it hard for consumers to interpret packaging. Some labels fail to 
              highlight allergens clearly, while others use vague warnings like 
              "may contain traces of...", leading to confusion.
            </p>
            
            <h4>Cross-Contamination During Manufacturing</h4>
            <p>
              Even if an allergen is not an intentional ingredient, it can still end 
              up in a product due to shared manufacturing equipment. Many food production 
              facilities process multiple items together, increasing the risk of 
              accidental allergen exposure.
            </p>
          </div>
          
          <div className="about-section">
            <h3>Our Solution</h3>
            <p>
              Nima AI is a smart application that scans food labels, restaurant menus, 
              and online food orders to detect allergens instantly. With just a simple 
              scan using a smartphone camera, the app extracts text from food packaging 
              using Optical Character Recognition (OCR) and cross-references the data 
              with an extensive food allergen database.
            </p>
            <p>
              By leveraging AI and machine learning, Nima AI ensures that users can 
              make safe, informed food choices, significantly reducing the risks of 
              allergic reactions and improving their quality of life.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default AboutPage;