<<<<<<< HEAD
export const initDateTime = () => {
  const updateDateTime = () => {
    const now = new Date();

    const options = {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    };
    const dateString = now.toLocaleDateString("id-ID", options);

    const timeString = now.toLocaleTimeString("id-ID");

    document.getElementById("current-date").textContent = dateString;
    document.getElementById("current-time").textContent = timeString;
  };

  updateDateTime();

  setInterval(updateDateTime, 1000);
};

export const getTodayName = () => {
  const days = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
  ];
  const today = new Date().getDay();
  return days[today];
};

export const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("id-ID", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
};

export const isDueSoon = (deadline) => {
  const today = new Date();
  const dueDate = new Date(deadline);
  const diffTime = dueDate - today;
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

  return diffDays >= 0 && diffDays <= 2;
};
=======
export const initDateTime = () => {
  const updateDateTime = () => {
    const now = new Date();

    const options = {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    };
    const dateString = now.toLocaleDateString("id-ID", options);

    const timeString = now.toLocaleTimeString("id-ID");

    document.getElementById("current-date").textContent = dateString;
    document.getElementById("current-time").textContent = timeString;
  };

  updateDateTime();

  setInterval(updateDateTime, 1000);
};

export const getTodayName = () => {
  const days = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
  ];
  const today = new Date().getDay();
  return days[today];
};

export const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("id-ID", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
};

export const isDueSoon = (deadline) => {
  const today = new Date();
  const dueDate = new Date(deadline);
  const diffTime = dueDate - today;
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

  return diffDays >= 0 && diffDays <= 2;
};
>>>>>>> 46ef116e4c333020536d97f8df7297f9452c8646
