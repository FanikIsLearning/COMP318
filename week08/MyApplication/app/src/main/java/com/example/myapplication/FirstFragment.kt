package com.example.myapplication

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.myapplication.databinding.FragmentFirstBinding

/**
 * A simple [Fragment] subclass as the default destination in the navigation.
 */
class FirstFragment : Fragment() {

    private var _binding: FragmentFirstBinding? = null

    // This property is only valid between onCreateView and onDestroyView.
    private val binding get() = _binding!!

    private fun countMe() {
        // Get the value of the text view.
        val countString = binding.textviewFirst.text.toString()

        // Convert value to a number and increment it
        var count = countString.toIntOrNull() ?: 0
        count++

        // Display the new value in the text view.
        binding.textviewFirst.text = count.toString()
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentFirstBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.randomButton.setOnClickListener {
            findNavController().navigate(R.id.action_FirstFragment_to_SecondFragment)
        }

        binding.toastButton.setOnClickListener {
            // create a Toast with some text, to appear for a short time
            val myToast = Toast.makeText(requireContext(), "Hello Toast!", Toast.LENGTH_SHORT)
            // show the Toast
            myToast.show()
        }

        binding.countButton.setOnClickListener {
            countMe()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
