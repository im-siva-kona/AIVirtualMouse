// src/Services.js

import React, { useState } from 'react';

function Services() {
  const [showPopup, setShowPopup] = useState(false);
  const [selectedService, setSelectedService] = useState(null);

  const services = [
    {
      name: 'Home Cleansing',
      image: 'logo192.png', // Add your image URL here or leave it empty for a placeholder
      price: '$100',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      workHours: '9 AM - 5 PM',
      arrivalTime: 'Within 24 hours'
    },
    {
      name: 'Photography',
      image: '',
      price: '$200',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      workHours: '10 AM - 6 PM',
      arrivalTime: 'Scheduled'
    },
    {
      name: 'Home Repair',
      image: '',
      price: '$150',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      workHours: '8 AM - 4 PM',
      arrivalTime: 'Within 48 hours'
    },
    {
      name: 'Construction',
      image: '',
      price: '$500',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      workHours: '8 AM - 6 PM',
      arrivalTime: 'Scheduled'
    },
    
    {
      name: 'Home Cleansing',
      image: 'logo192.png', // Add your image URL here or leave it empty for a placeholder
      price: '$100',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
      workHours: '9 AM - 5 PM',
      arrivalTime: 'Within 24 hours'
    },
  ];

  const handleCardClick = (service) => {
    setSelectedService(service);
    setShowPopup(true);
  };

  const closePopup = () => {
    setShowPopup(false);
  };

  return (
    <div className="flex flex-wrap justify-center mt-10">
      {services.map((service, index) => (
        <div key={index} className="max-w-md mx-4 mb-8 bg-white rounded-lg shadow-lg overflow-hidden cursor-pointer"
             onClick={() => handleCardClick(service)}>
          <div className="p-4">
            <h2 className="text-xl font-semibold mb-2">{service.name}</h2>
            <img src={service.image || 'https://via.placeholder.com/300x200'} alt={service.name} className="w-full h-auto mb-4" />
          </div>
        </div>
      ))}
      {showPopup && selectedService && (
        <div className="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75">
          <div className="bg-white p-8 max-w-lg rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">{selectedService.name}</h2>
            <p className="text-gray-700 mb-2">Price: {selectedService.price}</p>
            <p className="text-gray-700 mb-2">Description: {selectedService.description}</p>
            <p className="text-gray-700 mb-2">Work Hours: {selectedService.workHours}</p>
            <p className="text-gray-700 mb-4">Estimated Arrival Time: {selectedService.arrivalTime}</p>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                    onClick={closePopup}>
              Close
            </button>
            <button className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded ml-4">
              Book Now
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Services;
