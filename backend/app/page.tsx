const endpoints = [
  {
    name: "Health Check",
    path: "/api/health",
    description: "Check whether the backend is running.",
  },
  {
    name: "Database Test",
    path: "/api/db-test",
    description: "Test the connection between Next.js and Supabase.",
  },
  {
    name: "Devices",
    path: "/api/devices",
    description: "View registered Shelly devices.",
  },
  {
    name: "Measurements",
    path: "/api/measurements",
    description: "View stored electrical measurements.",
  },
];

export default function Home() {
  return (
    <main className="min-h-screen p-10">
      <div className="mx-auto max-w-4xl">
        <h1 className="text-4xl font-bold">
          WattWiser
        </h1>

        <p className="mt-3 text-gray-600">
          Just a sample dashboard to test the connections
        </p>

        <div className="mt-10 grid gap-4">
          {endpoints.map((endpoint) => (
            <a
              key={endpoint.path}
              href={endpoint.path}
              className="block rounded-lg border p-5 hover:bg-gray-50"
            >
              <h2 className="text-xl font-semibold">
                {endpoint.name}
              </h2>

              <p className="mt-1 text-sm text-gray-600">
                {endpoint.description}
              </p>

              <p className="mt-3 font-mono text-sm">
                http://localhost:3000{endpoint.path}
              </p>
            </a>
          ))}
        </div>
      </div>
    </main>
  );
}