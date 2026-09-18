import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    status: "healthy",
    service: "shelly-energy-backend",
    timestamp: new Date().toISOString(),
  });
}