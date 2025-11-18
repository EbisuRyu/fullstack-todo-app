import React from "react";

const NotFound = () => {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen text-center bg-slate-50">
      <img
        src="/404_NotFound.png"
        alt="Page not found"
        className="w-80 max-w-full mb-6"
      />

      <h1 className="text-2xl font-bold text-slate-700 mb-2">
        Page Not Found
      </h1>
      <p className="text-lg text-slate-500">
        This page does not exist
      </p>

      <a href="/" className="inline-block px-6 py-3 mt-6 font-medium text-white transition shadow-md bg-primary rounded-2xl hover:bg-primary-dark">
        Return to home page
      </a>
    </main>
  );
};

export default NotFound;
