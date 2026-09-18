// import { NextResponse } from "next/server";
// import { supabase } from "@/lib/supabase/client";

// export async function GET() {
//   const { data, error } = await supabase
//     .from("devices")
//     .select("*")
//     .limit(5);

//   if (error) {
//     return NextResponse.json(
//       {
//         success: false,
//         error: error.message,
//       },
//       { status: 500 }
//     );
//   }

//   return NextResponse.json({
//     success: true,
//     data,
//   });
// } 


import { NextResponse } from "next/server";
import { supabase } from "@/lib/supabase/client";

export async function GET() {
  const { data, error } = await supabase.rpc("get_current_role");

  return NextResponse.json({
    data,
    error,
  });
}